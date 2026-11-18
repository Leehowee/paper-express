/** Native editable PPTX + SVG library. No paper screenshots or flattened diagrams.
 * Requires @oai/artifact-tool. See references/running.md for portable invocation.
 * Geometry in assets/diagram-scenes.json is authoritative after --init-scenes.
 */
import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const args=process.argv.slice(2);
const opt=(k,fallback)=>args.includes(k)?args[args.indexOf(k)+1]:fallback;
const out=path.resolve(opt('--out',path.join(ROOT,'assets/native')));
const build=path.resolve(opt('--build',path.join(ROOT,'../../tmp/paper-figures-native')));
const runtime=process.env.ARTIFACT_NODE_MODULES;
const req=createRequire(runtime?path.join(runtime,'_resolver.cjs'):import.meta.url);
const {Presentation,PresentationFile,FileBlob}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const C={blue:'#0F4D92',pale:'#E8F0F8',teal:'#42949E',purple:'#9A4D8E',grey:'#F0F2F3',ink:'#263442',line:'#62717D'};
const W=1280,H=720;
function node(id,label,x,y,w,h,fill=C.pale,extra={}){return {id,label,x,y,w,h,fill,font:22,...extra};}
function text(id,label,x,y,w,h,font=20,extra={}){return node(id,label,x,y,w,h,'none',{font,stroke:'none',align:'left',...extra});}
function edge(from,to,extra={}){return {from,to,fromSide:'right',toSide:'left',...extra};}
function basic(id,title,note){return {id,title,note,nodes:[],edges:[]};}
function initScenes(){
  const scenes=[];
  let s=basic('D01-comparison','Matched method comparison','SCHEMATIC TEMPLATE · identical task and inputs · replace labels with sourced definitions');
  for(const [i,label] of ['Prior route','Proposed route'].entries()){
    const y=170+i*245,pre='r'+i;
    s.nodes.push(text(pre+'label',label,48,y+35,180,55,23,{bold:true,color:i?C.blue:C.ink}),node(pre+'in','Input X',235,y,160,120),node(pre+'rel',i?'Reliability\nmatrix':'Fixed relation\nmatrix',455,y,230,120,i?C.pale:C.grey),node(pre+'enc',i?'Weighted\nencoder':'Encoder',745,y,200,120),node(pre+'out','Output Y',1005,y,210,120));
    s.edges.push(edge(pre+'in',pre+'rel'),edge(pre+'rel',pre+'enc'),edge(pre+'enc',pre+'out'));
    s.nodes.push(text(pre+'assumption',i?'[Changed assumption / decision]':'[Required assumption / information]',250,y+135,930,45,19));
  }
  scenes.push(s);
  s=basic('D02-method','Method overview with an expanded focal module','SCHEMATIC TEMPLATE · solid: forward computation · dashed: training objective / update');
  s.nodes.push(node('input-a','Source A',45,200,165,80,'#E4F2F2'),node('input-b','Source B',45,355,165,80,'#F1E7F1'),node('encoder-a','Encoder A',265,200,180,80),node('encoder-b','Encoder B',265,355,180,80),node('novel','Focal module',535,190,360,255,C.pale,{bold:true,vertical:'top'}),node('condition','Condition / prior',565,85,300,65,C.grey),node('output','Prediction',990,270,235,90),node('loss','Loss (training only)',560,530,320,70,C.grey),text('formula','[Eq. / operation]\n[shape and normalization]',700,285,170,110,18));
  for(let y=0;y<4;y++)for(let x=0;x<4;x++)s.nodes.push(node(`matrix-${y}-${x}`,'',570+x*26,280+y*26,23,23,x===y?C.blue:'#BCD0E2',{stroke:'#FFFFFF'}));
  s.edges.push(edge('input-a','encoder-a'),edge('input-b','encoder-b'),edge('encoder-a','novel'),edge('encoder-b','novel'),edge('condition','novel',{fromSide:'bottom',toSide:'top'}),edge('novel','output'),edge('output','loss',{fromSide:'bottom',toSide:'right',dash:true}),edge('loss','encoder-a',{fromSide:'left',toSide:'bottom',dash:true}),edge('loss','encoder-b',{fromSide:'left',toSide:'bottom',dash:true}));
  scenes.push(s);
  s=basic('D03-temporal','Problem example: time and correspondence','SCHEMATIC TEMPLATE · replace placeholders with real frames, timestamps and verified annotations');
  s.nodes.push(text('frame-label','Frames',40,155,125,45,22,{bold:true}),text('text-label','Captions',40,335,125,45,22,{bold:true}));
  for(let i=0;i<5;i++){
    s.nodes.push(node('f'+i,`[Frame ${i+1}]`,175+i*205,140,175,100,C.grey),text('time'+i,`[time ${i+1}]`,175+i*205,250,90,35,16,{align:'left'}),node('t'+i,`[Caption ${i+1}]`,175+i*205,325,175,100,'#F0F6F8'));
    s.edges.push(edge('f'+i,'t'+i,{fromSide:'bottom',toSide:'top',dash:true}));
  }
  s.nodes.push(text('observed','Observed pairing: dashed arrows',175,485,900,42,20),text('annotation','[Annotate asynchronous / irrelevant / fine-grained mismatch here]',175,540,1000,55,21,{color:C.blue}));
  scenes.push(s);
  s=basic('D04-retrieval-cases','Case evidence: query, candidates and a retained failure','PLACEHOLDER TEMPLATE · retain sample IDs, selection rule, relevance labels and rank changes');
  for(let i=0;i<2;i++){
    const y=140+i*240;
    s.nodes.push(text('case'+i,i?'[Failure case ID]':'[Success case ID]',42,y,200,45,22,{bold:true}),node('query'+i,'[Query]\n[Criterion]',42,y+55,200,125,C.grey));
    for(let j=0;j<4;j++)s.nodes.push(node(`cand${i}${j}`,`[Candidate ${j+1}]\n[rank / relevance]`,290+j*225,y+35,195,135,j===0?C.pale:C.grey));
    s.nodes.push(text('reason'+i,'[Observed change and verified reason; separate model explanation from ground truth]',290,y+182,890,40,18));
  }
  scenes.push(s);
  s=basic('D06-compound','Compose one figure around one scientific question','LAYOUT TEMPLATE · each panel has a distinct role · preserve units, legends and evidence types');
  [['a','Controlled observation',48,135,555,210],['b','Mechanism diagnostic',650,135,580,210],['c','Intervention / ablation',48,395,555,210],['d','Boundary / failure case',650,395,580,210]].forEach(([id,label,x,y,w,h])=>{s.nodes.push(node(id,'',x,y,w,h,'#FAFBFC',{stroke:'#BCC8D2'}),text(id+'title',`${id}  ${label}`,x+15,y+10,w-30,40,22,{bold:true}),text(id+'fill','[Insert a data-generated plot or a documented case]',x+20,y+83,w-40,65,20));});
  scenes.push(s);
  return scenes;
}
const scenePath=path.join(ROOT,'assets/diagram-scenes.json');
if(args.includes('--init-scenes'))await fs.writeFile(scenePath,JSON.stringify(initScenes(),null,2));
const scenes=JSON.parse(await fs.readFile(scenePath,'utf8'));
await fs.mkdir(out,{recursive:true});await fs.mkdir(build,{recursive:true});
const font='Arial';
const p=Presentation.create({slideSize:{width:W,height:H}});
const fontPolicy={basis:'design',families:[font]};
function addShape(sl,n){
  const sh=sl.shapes.add({geometry:'rect',name:n.id,position:{left:n.x,top:n.y,width:n.w,height:n.h},fill:n.fill,line:{fill:n.stroke??C.line,width:n.stroke==='none'?0:1},borderRadius:n.radius??0});
  if(n.label){sh.text=n.label;sh.text.style={typeface:font,fontSize:n.font??22,bold:n.bold??false,color:n.color??C.ink,alignment:n.align??'center',verticalAlignment:n.vertical??'middle',autoFit:'none',insets:8,wrap:'square'};}
  return sh;
}
function page(id,title,note){const sl=p.slides.add();sl.background.fill='#FFFFFF';addShape(sl,text(id+'title',title,40,26,1200,65,28,{bold:true}));addShape(sl,text(id+'note',note,42,654,1195,45,17,{color:'#64717D'}));return sl;}
function anchor(n,side){return side==='left'?[n.x,n.y+n.h/2]:side==='right'?[n.x+n.w,n.y+n.h/2]:side==='top'?[n.x+n.w/2,n.y]:[n.x+n.w/2,n.y+n.h];}
function esc(x){return String(x).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');}
function svgText(n){
  const maxChars=Math.max(4,Math.floor((n.w-16)/((n.font??22)*.53)));const lines=[];
  for(const paragraph of n.label.split('\n')){let line='';for(const word of paragraph.split(' ')){if(line&&line.length+word.length+1>maxChars){lines.push(line);line=word;}else line+=(line?' ':'')+word;}lines.push(line);}
  let x=n.align==='left'?n.x+8:n.x+n.w/2;let y=n.vertical==='top'?n.y+n.font+10:n.y+n.h/2-(lines.length-1)*n.font*.6+n.font*.32;
  return `<text x="${x}" y="${y}" fill="${n.color??C.ink}" font-family="Arial,sans-serif" font-size="${n.font??22}" font-weight="${n.bold?'700':'400'}" text-anchor="${n.align==='left'?'start':'middle'}">${lines.map((l,i)=>`<tspan x="${x}" dy="${i?n.font*1.2:0}">${esc(l)}</tspan>`).join('')}</text>`;
}
function svgEdgePath(a,b,fromSide,toSide){
  const vec={left:[-1,0],right:[1,0],top:[0,-1],bottom:[0,1]},u=vec[fromSide],v=vec[toSide];
  if((a[0]===b[0]&&u[0]===0&&v[0]===0)||(a[1]===b[1]&&u[1]===0&&v[1]===0))return `M ${a} L ${b}`;
  const s=[a[0]+u[0]*24,a[1]+u[1]*24],t=[b[0]+v[0]*24,b[1]+v[1]*24];
  const midX=fromSide==='left'&&toSide==='bottom'?s[0]-64:(s[0]+t[0])/2;
  const middle=u[0]!==0?`L ${midX} ${s[1]} L ${midX} ${t[1]}`:`L ${s[0]} ${(s[1]+t[1])/2} L ${t[0]} ${(s[1]+t[1])/2}`;
  return `M ${a} L ${s} ${middle} L ${t} L ${b}`;
}
function svgScene(s){
  let chunks=[`<svg xmlns="http://www.w3.org/2000/svg" width="180mm" height="101.25mm" viewBox="0 0 ${W} ${H}"><title>${esc(s.title)}</title><desc>Editable conceptual template; no experimental data.</desc><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="${C.line}"/></marker></defs><rect width="1280" height="720" fill="white"/>`];
  for(const e of s.edges){const a=anchor(s.nodes.find(n=>n.id===e.from),e.fromSide),b=anchor(s.nodes.find(n=>n.id===e.to),e.toSide);const d=svgEdgePath(a,b,e.fromSide,e.toSide);chunks.push(`<path d="${d}" fill="none" stroke="${C.line}" stroke-width="2" ${e.dash?'stroke-dasharray="7 5"':''} marker-end="url(#arrow)"/>`);}
  const ns=[...s.nodes,text(s.id+'title',s.title,40,26,1200,65,28,{bold:true}),text(s.id+'note',s.note,42,654,1195,45,17,{color:'#64717D'})];
  for(const n of ns){chunks.push(`<g id="${esc(n.id)}"><rect x="${n.x}" y="${n.y}" width="${n.w}" height="${n.h}" fill="${n.fill}" stroke="${n.stroke??C.line}" stroke-width="1"/>${n.label?svgText(n):''}</g>`);}
  return chunks.join('\n')+'</svg>';
}
const slideIds=[];
for(const scene of scenes.slice(0,4)){
  const sl=page(scene.id,scene.title,scene.note);const shapes={};for(const n of scene.nodes)shapes[n.id]=addShape(sl,n);
  for(const e of scene.edges)sl.shapes.connect(shapes[e.from],shapes[e.to],{kind:'elbow',fromSide:e.fromSide,toSide:e.toSide,line:{fill:C.line,width:2,style:e.dash?'dashed':'solid'},tail:{type:'triangle',width:'sm',length:'sm'}});
  sl.speakerNotes.text='Original generic template. Source reasoning patterns: XP03 Fig.1–2; XP04 Fig.1–2; XP05 Fig.1–3; XP06 Fig.11–15. See references/source-index.md. Concept image used only as layout reference; erroneous extra encoder-to-encoder arrow removed. No measured evidence.';
  slideIds.push(scene.id);await fs.writeFile(path.join(out,scene.id+'.svg'),svgScene(scene));
}
function nativeTable(sl,headers,rows,groupRows=[],widths=null){
  const t=sl.tables.add({rows:rows.length+1,columns:headers.length,left:48,top:145,width:1184,height:Math.min(430,(rows.length+1)*51),values:[headers.map(x=>x.replaceAll('\n',' / ')),...rows],columnWidths:widths??[290,...Array(headers.length-1).fill(894/(headers.length-1))]});
  t.borders.assign({fill:'#BCC6CE',width:.6});
  for(let i=0;i<=rows.length;i++)for(let j=0;j<headers.length;j++){
    const cell=t.getCell(i,j);cell.text.style={typeface:font,fontSize:20,color:C.ink,bold:i===0||groupRows.includes(i-1),alignment:j===0?'left':'center',verticalAlignment:'middle',insets:8};cell.fill=i===0?C.pale:groupRows.includes(i-1)?'#F3F5F6':'#FFFFFF';
  }
  for(const i of groupRows)t.merge({startRow:i+1,endRow:i+1,startColumn:0,endColumn:headers.length-1});
  return t;
}
let sl=page('D05-capability','Capability and assumptions table','PLACEHOLDER TEMPLATE · statuses require criterion-specific evidence · Unknown is not No');
const capabilityHeaders=['Route','Required information','Capability A','Capability B','Evidence'];
const capabilityRows=[['[Prior A]','[Labels / prior]','Yes','Partial','[Source]'],['[Prior B]','[Unlabelled data]','Unknown','Yes','[Source]'],['[Proposed]','[Actual assumption]','[Status]','[Status]','[Section]']];
const capabilityWidths=[205,340,180,180,279];
nativeTable(sl,capabilityHeaders,capabilityRows,[],capabilityWidths);
const capabilityScene=basic('D05-capability','Capability and assumptions table','PLACEHOLDER TEMPLATE · statuses require criterion-specific evidence · Unknown is not No');
for(const [r,row] of [capabilityHeaders,...capabilityRows].entries()){
  let x=48;for(const [j,value] of row.entries()){
    capabilityScene.nodes.push(node(`cell-${r}-${j}`,value,x,145+r*51,capabilityWidths[j],51,r===0?C.pale:'#FFFFFF',{font:20,bold:r===0,align:j===0?'left':'center',stroke:'#BCC6CE'}));x+=capabilityWidths[j];
  }
}
await fs.writeFile(path.join(out,'D05-capability.svg'),svgScene(capabilityScene));
sl.speakerNotes.text='A capability table is an evidence-backed taxonomy, not a performance ranking. Inspired by GH06 Fig.2c and XP04 Fig.1. Placeholder statuses do not describe any real method.';slideIds.push('D05-capability');
for(const id of ['T01-main','T02-ablation','T03-parameter','T04-efficiency']){
  const d=JSON.parse(await fs.readFile(path.join(ROOT,'assets/gallery',id+'.table.json'),'utf8'));
  const sl=page(id,id.replaceAll('-',' '),'SYNTHETIC DATA · editable native table · regenerate from CSV when values change');
  const nt=nativeTable(sl,d.headers,d.rows,d.group_rows,d.column_widths?d.column_widths.map(w=>w*1184):null);
  for(const [r,c] of d.best_cells??[])nt.getCell(r,c).text.style={typeface:font,fontSize:20,bold:true,color:C.ink,alignment:'center'};
  addShape(sl,text(id+'rank-note','Bold: best displayed mean within each comparable block; ties retained. Not a significance test.',48,532,1170,40,17));
  addShape(sl,text(id+'caption',d.caption.split(' Bold:')[0],48,580,1170,65,17));
  sl.speakerNotes.text=d.caption+' Source: assets/examples/configs/'+id+'.json and corresponding raw CSV. Native table values derive from assets/gallery/'+id+'.table.json.';
  slideIds.push(id);
}
sl=page('F12-native-chart','Component weights: editable native chart','SYNTHETIC DATA · normalized weights · y-axis starts at zero · chart has an embedded workbook');
// Parse this deliberately simple example CSV; quoted labels require a full CSV parser.
const weightConfig=JSON.parse(await fs.readFile(path.join(ROOT,'assets/examples/configs/F12-weights.json'),'utf8'));
const weightLines=(await fs.readFile(path.join(ROOT,'assets/examples/data/F12-weights.csv'),'utf8')).trim().split(/\r?\n/).slice(1).map(l=>l.split(','));
if(weightLines.some(r=>r.length!==3))throw Error('Expected simple series,component,value CSV for native chart');
const weightSeries=weightConfig.series.map((name,i)=>({name,fill:[C.blue,C.teal,C.purple][i%3],values:weightConfig.components.map(k=>{
  const rr=weightLines.filter(r=>r[0]===name&&r[1]===k);if(rr.length!==1||!Number.isFinite(Number(rr[0][2])))throw Error('Invalid native chart data');return Number(rr[0][2]);
})}));
const chart=sl.charts.add('bar',{position:{left:140,top:130,width:1000,height:470},categories:weightConfig.components,series:weightSeries,barOptions:{direction:'column',grouping:'clustered',gapWidth:95},hasLegend:true,legend:{position:'bottom',textStyle:{typeface:font,fontSize:20}},xAxis:{textStyle:{typeface:font,fontSize:20},title:{text:'Component',textStyle:{typeface:font,fontSize:20}}},yAxis:{min:0,max:weightConfig.ymax,majorUnit:.1,numberFormatCode:'0.0',textStyle:{typeface:font,fontSize:20},title:{text:'Normalized weight',textStyle:{typeface:font,fontSize:20}},majorGridlines:{fill:'#E0E6EB',width:.7}},chartFill:'#FFFFFF',plotAreaFill:'#FFFFFF'});
sl.speakerNotes.text='Exact literal values from F12-weights.csv. A single deterministic synthetic vector per series; no uncertainty claimed. Use the Python route for uncertainty from independent runs. Native chart is not an SVG picture.';slideIds.push('F12-native-chart');
const scene=scenes[4];sl=page(scene.id,scene.title,scene.note);for(const n of scene.nodes)addShape(sl,n);slideIds.push(scene.id);await fs.writeFile(path.join(out,scene.id+'.svg'),svgScene(scene));
const candidate=path.join(build,'candidate.pptx');await (await PresentationFile.exportPptx(p)).save(candidate);
const delivered=path.join(out,'paper-figure-table-templates.pptx');
try{await fs.access(delivered);if(!args.includes('--replace'))throw Error('Output exists; use a new --out directory or explicit --replace');}catch(e){if(e.code!=='ENOENT')throw e;}
await fs.mkdir(path.join(build,'delivery'),{recursive:true});
const buildId=Date.now();
let finalPath=path.join(build,'delivery',`validated-${buildId}.pptx`);
if(process.env.PRESENTATION_SKILL_DIR&&process.env.RUNTIME_PYTHON){
  const skill=process.env.PRESENTATION_SKILL_DIR;
  const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
  const receiptPath=path.join(build,`validation-${buildId}.json`);
  await finalizePresentation({workspaceDir:path.resolve(ROOT,'../..'),candidatePath:candidate,finalPath,pythonExecutable:process.env.RUNTIME_PYTHON,integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit',...[5,6,7,8,9].flatMap(n=>['--require-native-table-slide',String(n)])],explicitTotalSlideCount:11,requiredNativeTableOwnerSlides:[5,6,7,8,9],requiredNativeChartOwnerSlides:[10],materializeLiteralChartWorkbooks:true,fontPolicy,verifyArtifactToolImport:true,receiptPath});
  await fs.copyFile(receiptPath,path.join(build,'validation.json'));
}else{await fs.copyFile(candidate,finalPath);console.warn('Export only: bundled finalizer not configured. Run package validation before delivery.');}
await fs.copyFile(finalPath,delivered);
// Render the exported artifact after reimport, not just the source scene.
const final=await PresentationFile.importPptx(await FileBlob.load(finalPath));
for(const [i,slide] of final.slides.items.entries()){
  const image=await final.export({slide,format:'png',scale:1});await fs.writeFile(path.join(out,`${String(i+1).padStart(2,'0')}-${slideIds[i]}.png`),new Uint8Array(await image.arrayBuffer()));
}
await fs.writeFile(path.join(out,'slides.json'),JSON.stringify(slideIds.map((id,i)=>({slide:i+1,id})),null,2));
console.log(delivered);
if(args.includes('--editability-check')){
  const s=final.slides.items[0];const sh=s.shapes.items.find(x=>x.name==='r0in');
  if(!sh)throw Error('Editable shape not recovered after PPTX import');
  sh.text='EDIT CHECK';sh.position={...sh.position,left:sh.position.left+12};sh.fill='#DDF3DE';
  final.slides.items[5].tables.items[0].getCell(0,0).value='EDIT TABLE';
  final.slides.items[9].charts.items[0].series.getItemAt(0).values=[.11,.12,.13,.15,.49];
  const copy=path.join(build,'editability-copy.pptx');await (await PresentationFile.exportPptx(final)).save(copy);
  const re=await PresentationFile.importPptx(await FileBlob.load(copy));const changed=re.slides.items[0].shapes.items.find(x=>x.name==='r0in');
  const inspected=await re.inspect({kind:'shape,textbox',search:'EDIT CHECK',maxChars:2000});
  if(!inspected.ndjson.includes('EDIT CHECK'))throw Error('Edited label did not persist');
  if(Math.abs(changed.position.left-sh.position.left)>.1)throw Error('Moved geometry did not persist');
  const tableInspected=await re.inspect({kind:'table',search:'EDIT TABLE',maxChars:2000});
  if(!tableInspected.ndjson.includes('EDIT TABLE'))throw Error('Edited table cell did not persist');
  if(Math.abs(re.slides.items[9].charts.items[0].series.getItemAt(0).values[0]-.11)>1e-9)throw Error('Edited chart data did not persist');
  const png=await re.export({slide:re.slides.items[0],format:'png',scale:1});await fs.writeFile(path.join(build,'editability-after.png'),new Uint8Array(await png.arrayBuffer()));
  await fs.writeFile(path.join(build,'editability.json'),JSON.stringify({tool:'@oai/artifact-tool',label_changed:true,geometry_moved:true,table_cell_changed:true,chart_data_changed:true,roundtrip_passed:true,powerpoint_gui_tested:false,source_kept_unchanged:true},null,2));
}
