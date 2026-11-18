"""Validate template assets and scientific-data contracts; not a research replication.

Run after render_all.py and the native build. No GUI/visual-review claim is inferred.
"""
from __future__ import annotations
import argparse, ast, copy, csv, hashlib, io, json, math, platform, re, statistics, tempfile, zipfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote
import xml.etree.ElementTree as ET
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import PIL
from PIL import Image
import figurekit as fk
import tablekit as tk

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parents[1]
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','c':'http://schemas.openxmlformats.org/drawingml/2006/chart','s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
checks=[]

def check(condition, message):
    if not condition: raise AssertionError(message)
    checks.append(message)

def reject(name,fn):
    try: fn()
    except ValueError as e: checks.append('Rejected '+name+': '+str(e));return
    finally: plt.close('all')
    raise AssertionError('Unsafe input accepted: '+name)

def read_json(p):return json.loads(Path(p).read_text(encoding='utf-8'))
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def config(id):
    p=ROOT/'assets/examples/configs'/f'{id}.json';c=read_json(p)
    return c,fk.read_csv(p.parent/c['data']),p

def links(check_external=False):
    count=0
    for p in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            target=target.strip('<>').split('#')[0]
            if not target or re.match(r'[a-zA-Z]+:',target):continue
            if not (p.parent/unquote(target)).resolve().is_relative_to(ROOT) and not check_external:continue
            check((p.parent/unquote(target)).exists(),f'Link exists: {p.relative_to(ROOT)} → {target}');count+=1
    for p in (ROOT/'scripts').glob('*.py'):ast.parse(p.read_text(encoding='utf-8'))
    for rel in re.findall(r'(?m)^\s*(?:-\s*)?(?:\w+:\s*)?((?:static|assets|interfaces|references)/[\w./-]+)',(ROOT/'manifest.yaml').read_text(encoding='utf-8')):
        check((ROOT/rel).exists(),'Manifest target: '+rel)
    return count

def assets():
    configs=sorted((ROOT/'assets/examples/configs').glob('*.json'))
    check(len(configs)==16,'Sixteen ready-to-run configurations')
    table_cells=0
    for cp in configs:
        c=read_json(cp);id=c['id'];g=ROOT/'assets/gallery';audit=read_json(g/f'{id}.audit.json')
        check(c['synthetic'] is True and audit['synthetic'] is True,id+': synthetic status retained')
        check(bool(audit.get('generator_sha256')),id+': generation code recorded')
        for name,h in audit['generator_sha256'].items():
            check(digest(ROOT/'scripts'/name)==h,id+': generation code hash '+name)
        for name,h in audit['source_sha256'].items():
            source=g/name if audit.get('source_path_base')=='audit_directory' else Path(name)
            check(source.exists() and digest(source)==h,id+': source hash '+source.name)
        with Image.open(g/f'{id}.png') as im:
            expected=[c[k]/25.4*c['dpi'] for k in ['width_mm','height_mm']]
            check(all(abs(a-b)<2 for a,b in zip(im.size,expected)),id+': PNG physical size/dpi')
        svg=ET.parse(g/f'{id}.svg').getroot()
        check(len(svg.findall('.//{http://www.w3.org/2000/svg}text'))>0,id+': SVG contains editable text')
        width=float(svg.attrib['width'].replace('pt',''))*25.4/72
        check(abs(width-c['width_mm'])<.01,id+': SVG width')
        pdf=(g/f'{id}.pdf').read_bytes()
        mb=re.search(rb'/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)\s*\]',pdf)
        check(mb is not None and all(abs(float(v)*25.4/72-c[k])<.01 for v,k in zip(mb.groups(),['width_mm','height_mm'])),id+': PDF MediaBox')
        check(len(re.findall(rb'/Type\s*/Page\b',pdf))==1,id+': single-page PDF')
        if c['kind']=='table':
            d=read_json(g/f'{id}.table.json');buckets=defaultdict(list)
            for r in fk.read_csv(cp.parent/c['data']):
                if r['status']=='ok':buckets['|'.join(r[k] for k in ['group','method','dataset','metric'])].append(float(r['value']))
            for key,vals in buckets.items():
                got=d['cells'][key]
                check(math.isclose(got['mean'],statistics.mean(vals),abs_tol=1e-10) and math.isclose(got['sd'],statistics.stdev(vals),abs_tol=1e-10) and got['n']==len(vals),id+': independently recomputed '+key);table_cells+=1
            tex=(g/f'{id}.tex').read_text(encoding='utf-8')
            check(all(x in tex for x in [r'\toprule',r'\midrule',r'\bottomrule',r'\begin{tabular}',r'\end{tabular}']),id+': booktabs structure (not TeX compilation)')
    main=read_json(ROOT/'assets/gallery/T01-main.table.json')
    check(main['ranks']['matched|Baseline B|Set B|ACC']==main['ranks']['matched|Proposed|Set B|ACC']==1,'Displayed tie retained')
    check(not any(k.startswith('extra|') for k in main['ranks']),'Extra supervision reference excluded from ranking')
    check('OOM' in (ROOT/'assets/gallery/T01-main.csv').read_text(encoding='utf-8'),'OOM retained as status, not zero')
    cost=read_json(ROOT/'assets/gallery/T04-efficiency.table.json')
    check(cost['ranks']['device|Small|Inference|latency']==1 and cost['ranks']['device|Large|Inference|ACC']==1,'Metric-specific down/up ranking')
    c,rr,_=config('F04-ablation');full={r['run']:float(r['value']) for r in rr if r['series']=='Full'};a=read_json(ROOT/'assets/gallery/F04-ablation.audit.json')['summary']
    for s in c['series']:
        ds=[full[r['run']]-float(r['value']) for r in rr if r['series']==s]
        check(math.isclose(a[s]['delta_full_minus_variant'],statistics.mean(ds),abs_tol=1e-9) and math.isclose(a[s]['paired_sd'],statistics.stdev(ds),abs_tol=1e-9),'Paired difference recomputed: '+s)
    check(a['Frozen update']['delta_full_minus_variant']<0,'Adverse ablation preserved')
    return table_cells

def contracts():
    before=sum(item.startswith('Rejected ') for item in checks)
    base=[{'series':'A','run':'1','value':'1','status':'ok'},{'series':'A','run':'2','value':'3','status':'ok'}]
    reject('one run for SD',lambda:fk.aggregate(base[:1],['series']))
    reject('duplicate independent run',lambda:fk.aggregate(base+[base[0]],['series']))
    reject('NaN measurement',lambda:fk.number('nan','value'))
    reject('failed run silently removed',lambda:fk.aggregate([base[0],{**base[1],'status':'error'}],['series']))
    c,d,_=config('F04-ablation');d=[r for r in d if not(r['series']=='No reliability' and r['run']=='3')]
    reject('unmatched paired IDs',lambda:fk.ablation(c,d))
    c,d,_=config('F07-sensitivity-1d');d[0]['x']='0'
    reject('zero on log x',lambda:fk.curves(c,d))
    c,d,_=config('F01-motivation');d.append({**d[0],'series':'Hidden'})
    reject('undeclared curve series',lambda:fk.curves(c,d))
    c,d,_=config('F08-sensitivity-2d')
    reject('unreported heatmap cell',lambda:fk.heatmap(c,d[:-1]))
    d[0].update(status='unknown-code',value='')
    reject('unrecognized missing code',lambda:fk.heatmap(c,d))
    c,d,_=config('F12-weights');d[0]['value']='.8'
    reject('invalid normalized weights',lambda:fk.weights(c,d))
    c,d,_=config('F13-embedding')
    reject('unmatched embedding sample IDs',lambda:fk.embedding(c,d[:-1]))
    c,d,p=config('F14-cases');d[0]['roi_x']='51'
    reject('unmatched case ROI',lambda:fk.cases(c,d,p.parent))
    c,d,p=config('T01-main');d[0].update(status='error',value='')
    with tempfile.TemporaryDirectory(prefix='paper-figure-contract-') as temp:
        scratch=Path(temp).resolve()
        check(scratch.is_relative_to(Path(tempfile.gettempdir()).resolve()),'Contract-test temporary directory stays inside system temp')
        with (scratch/'data.csv').open('w',encoding='utf-8',newline='') as f:
            wr=csv.DictWriter(f,fieldnames=list(d[0]));wr.writeheader();wr.writerows(d)
        c['data']='data.csv';(scratch/'config.json').write_text(json.dumps(c),encoding='utf-8')
        reject('mixed success/failure table aggregation',lambda:tk.make_table(scratch/'config.json',scratch/'out'))
        (scratch/'duplicate.csv').write_text('series,run,value,value,status\nA,1,10,90,ok\n',encoding='utf-8')
        reject('duplicate CSV header overwriting data',lambda:fk.read_csv(scratch/'duplicate.csv'))
        (scratch/'short.csv').write_text('series,run,value,status\nA,1,10\n',encoding='utf-8')
        reject('short CSV row',lambda:fk.read_csv(scratch/'short.csv'))
        (scratch/'long.csv').write_text('series,run,value,status\nA,1,10,ok,extra\n',encoding='utf-8')
        reject('long CSV row',lambda:fk.read_csv(scratch/'long.csv'))
        (scratch/'empty.csv').write_text('series,,value\nA,1,10\n',encoding='utf-8')
        reject('empty CSV header',lambda:fk.read_csv(scratch/'empty.csv'))
        with (scratch/'quoted.csv').open('w',encoding='utf-8',newline='') as f:
            wr=csv.writer(f);wr.writerow(['label','value']);wr.writerow(['A | B, "quoted"\nsecond line','3.5'])
        check(fk.read_csv(scratch/'quoted.csv')==[{'label':'A | B, "quoted"\nsecond line','value':'3.5'}],'Quoted CSV preserves labels and values')
        reject('empty independent run ID',lambda:fk.aggregate([{**base[0],'run':''},base[1]],['series']))
        reject('numeric overflow in mean/SD',lambda:fk.aggregate([{**r,'value':'1e308'} for r in base],['series']))
        tc,_,tcp=config('T01-main');tc['data']=str((tcp.parent/tc['data']).resolve());tc['formats']=['svg']
        bad=copy.deepcopy(tc);bad['columns'].append(copy.deepcopy(bad['columns'][0]))
        reject('duplicate result column',lambda:tk.validate_table(bad))
        bad=copy.deepcopy(tc);bad['groups'].append(copy.deepcopy(bad['groups'][0]))
        reject('duplicate comparison group',lambda:tk.validate_table(bad))
        bad=copy.deepcopy(tc);bad['groups'][0]['methods'].append(copy.deepcopy(bad['groups'][0]['methods'][0]))
        reject('duplicate method ID',lambda:tk.validate_table(bad))
        bad=copy.deepcopy(tc);bad['synthetic']='false'
        reject('string synthetic flag',lambda:tk.validate_table(bad))
        bad=copy.deepcopy(tc);bad['groups'][0]['rank']='false'
        reject('string ranking flag',lambda:tk.validate_table(bad))
        bad=copy.deepcopy(tc);bad['id']='../outside-output'
        reject('output identifier containing a directory',lambda:tk.validate_table(bad))
        bad,_,_=config('F01-motivation');bad['panels'].append(copy.deepcopy(bad['panels'][0]))
        reject('duplicate panel ID',lambda:fk.validate_config(bad))
        bad,_,_=config('F08-sensitivity-2d');bad['panels'][0]['x_values'].append(bad['panels'][0]['x_values'][0])
        reject('duplicate heatmap coordinate',lambda:fk.validate_config(bad))
        label='A | B, "quoted"\nsecond line'
        tc['groups'][0]['methods'][0]['label']=label
        (scratch/'quoted-table.json').write_text(json.dumps(tc),encoding='utf-8')
        tk.make_table(scratch/'quoted-table.json',scratch/'quoted-table')
        generated_audit=read_json(scratch/'quoted-table'/f'{tc["id"]}.audit.json')
        for name,h in generated_audit['source_sha256'].items():
            source=scratch/'quoted-table'/name
            check(source.exists() and digest(source)==h,'Temporary-output provenance resolves: '+source.name)
        payload=read_json(scratch/'quoted-table'/f'{tc["id"]}.table.json')
        check(payload['rows'][1][0]==label,'Native table payload retains arbitrary quoted method label')
        md=(scratch/'quoted-table'/f'{tc["id"]}.md').read_text(encoding='utf-8')
        check('A &#124; B, "quoted"<br>second line' in md,'Markdown label cannot create an extra table column')
        with (scratch/'quoted-table'/f'{tc["id"]}.csv').open(encoding='utf-8',newline='') as f:
            check(list(csv.reader(f))[2][0]==label,'CSV export retains multiline method label')
    return sum(item.startswith('Rejected ') for item in checks)-before

def pptx():
    p=ROOT/'assets/native/paper-figure-table-templates.pptx'
    counts={}
    with zipfile.ZipFile(p) as z:
        names=z.namelist();slides=[n for n in names if re.fullmatch(r'ppt/slides/slide\d+\.xml',n)]
        check(len(slides)==11,'Native PPTX has eleven slides')
        allxml={int(re.search(r'(\d+)\.xml',n)[1]):ET.fromstring(z.read(n)) for n in slides}
        tables=sum(len(t.findall('.//a:tbl',NS)) for t in allxml.values());pics=sum(len(t.findall('.//p:pic',NS)) for t in allxml.values())
        check(tables==5,'Five native PPTX tables');check(pics==0,'No flattened picture substitutes in native PPTX')
        for page,id in enumerate(['T01-main','T02-ablation','T03-parameter','T04-efficiency'],6):
            d=read_json(ROOT/f'assets/gallery/{id}.table.json');tbl=allxml[page].find('.//a:tbl',NS);rows=tbl.findall('a:tr',NS)
            want=[[h.replace('\n',' / ') for h in d['headers']],*d['rows']]
            check(len(rows)==len(want),id+': native row count')
            for i,(row,expected) in enumerate(zip(rows,want)):
                cells=row.findall('a:tc',NS)
                got=[''.join(t.text or '' for t in cell.findall('.//a:t',NS)) for cell in cells]
                if i-1 in d['group_rows']:check(got[0]==expected[0],id+': native group '+str(i))
                else:check(got==expected,id+': native values row '+str(i))
            for r,c in d['best_cells']:
                check(any(n.attrib.get('b')=='1' for n in rows[r].findall('a:tc',NS)[c].findall('.//a:rPr',NS)),id+': native bold '+str((r,c)))
        scenes=read_json(ROOT/'assets/diagram-scenes.json')
        for page,scene in enumerate(scenes[:3],1):
            x=allxml[page];mapping={n.attrib['id']:n.attrib.get('name') for n in x.findall('.//p:sp/p:nvSpPr/p:cNvPr',NS)}
            pairs=set()
            for cn in x.findall('.//p:cxnSp',NS):
                start=cn.find('.//a:stCxn',NS);end=cn.find('.//a:endCxn',NS)
                if start is not None and end is not None:pairs.add((mapping[start.attrib['id']],mapping[end.attrib['id']]))
                check(cn.find('.//a:tailEnd',NS).attrib.get('type')=='triangle','Native connector arrowhead at destination')
            check(pairs=={(e['from'],e['to']) for e in scene['edges']},scene['id']+': connector endpoints match source definition')
        chart_names=[n for n in names if '/charts/' in n and n.endswith('.xml') and '/_rels/' not in n]
        charts=[ET.fromstring(z.read(n)) for n in chart_names];charts=[x for x in charts if x.find('.//c:chart',NS) is not None]
        check(len(charts)==1,'One native chart')
        series=charts[0].findall('.//c:barChart/c:ser',NS)
        c,d,_=config('F12-weights')
        for i,s in enumerate(series):
            vals=[float(n.text) for n in s.findall('c:val//c:pt/c:v',NS)]
            expected=[float(next(r['value'] for r in d if r['series']==c['series'][i] and r['component']==k)) for k in c['components']]
            check(np.allclose(vals,expected),'Native chart cache equals raw CSV: '+c['series'][i])
        books=[n for n in names if n.endswith('.xlsx')]
        check(len(books)==1,'Native chart contains an embedded editable workbook')
        with zipfile.ZipFile(io.BytesIO(z.read(books[0]))) as wb:
            numbers=[]
            for n in wb.namelist():
                if re.fullmatch(r'xl/worksheets/sheet\d+\.xml',n):
                    for cell in ET.fromstring(wb.read(n)).findall('.//s:c',NS):
                        v=cell.find('s:v',NS)
                        if v is not None and cell.attrib.get('t') not in {'s','str','b','e'}:numbers.append(float(v.text))
            check(np.allclose(sorted(numbers),sorted(float(r['value']) for r in d)),'Embedded workbook numbers equal raw CSV')
        counts={'slides':len(slides),'native_tables':tables,'native_charts':len(charts),'flattened_pictures':pics}
    for f in (ROOT/'assets/native').glob('D*.svg'):
        x=ET.parse(f).getroot();check(x.attrib['width']=='180mm' and len(x.findall('.//{http://www.w3.org/2000/svg}text'))>0,f.name+': standalone editable SVG')
    check(len(list((ROOT/'assets/native').glob('D*.svg')))==6,'Six native SVG templates')
    return counts

def sources():
    corpus=read_json(ROOT/'references/corpus-manifest.json')
    check(len(corpus['papers'])==22 and sum(len(p['visually_reviewed_pdf_pages']) for p in corpus['papers'])==73,'Source manifest records twenty-two papers and seventy-three selected pages')
    for p in corpus['papers']:check(digest(WORK/p['path_from_workspace'])==p['sha256'],'Source hash: '+p['id'])
    u=read_json(ROOT/'references/upstream-manifest.json');check(digest(WORK/u['archive'])==u['sha256'],'Upstream archive hash')
    with zipfile.ZipFile(WORK/u['archive']) as z:
        check(z.read('figures4papers-main/LICENSE')==(ROOT/'licenses/figures4papers-CC-BY-NC-4.0.txt').read_bytes(),'Upstream license preserved verbatim')

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check-sources',action='store_true');ap.add_argument('--native-receipts',type=Path);ap.add_argument('--report',type=Path,default=ROOT/'references/validation-report.json');args=ap.parse_args()
    nlinks=links(args.check_sources);ncells=assets();nrejects=contracts();native=pptx()
    receipt_summary=None
    if args.native_receipts:
        r=read_json(args.native_receipts/'validation.json');e=read_json(args.native_receipts/'editability.json')
        check(r['finalSha256']==digest(ROOT/'assets/native/paper-figure-table-templates.pptx'),'Final PPTX matches verified receipt')
        check(r['packageIntegrity']['status']=='pass' and r['presentationLayout']['finding_count']==0 and r['firstPartyImport']['passed'],'Finalizer structural/layout/import checks')
        check(all(e.get(k) for k in ['label_changed','geometry_moved','table_cell_changed','chart_data_changed','roundtrip_passed']),'Native editing and roundtrip passed')
        receipt_summary={'structural_pass':True,'layout_findings':0,'editable_roundtrip':e,'powerpoint_gui_tested':False}
    if args.check_sources:sources()
    hashes={p.relative_to(ROOT).as_posix():digest(p) for base in ['assets','scripts'] for p in (ROOT/base).rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    report={'verified_at_utc':datetime.now(timezone.utc).isoformat(),'status':'pass','python':platform.python_version(),'matplotlib':matplotlib.__version__,'numpy':np.__version__,'pillow':PIL.__version__,'links_checked':nlinks,'table_cells_independently_recomputed':ncells,'negative_input_cases':nrejects,'native':native,'native_receipts':receipt_summary,'source_hashes_checked':args.check_sources,'checks':checks,'artifact_sha256':hashes,'limits':['Visual inspection is separately recorded; not inferred from this script.','No PowerPoint GUI execution.','No LaTeX engine compilation.','No reproduction of source-paper experiments.']}
    args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','links_checked','table_cells_independently_recomputed','negative_input_cases','native']},ensure_ascii=False))

if __name__=='__main__':main()
