"""Generate consistent CSV/Markdown/LaTeX/SVG/PDF/PNG paper tables from run data."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from figurekit import aggregate, distinct_labels, finish, number, read_csv, style, unique, validate_config


def tex_escape(s):
    mapping={"\\":r"\textbackslash{}","&":r"\&","%":r"\%","$":r"\$","#":r"\#","_":r"\_","{":r"\{","}":r"\}","~":r"\textasciitilde{}","^":r"\textasciicircum{}","↑":r"$\uparrow$","↓":r"$\downarrow$","±":r"$\pm$","−":"-"}
    return "".join(mapping.get(ch,ch) for ch in str(s))


def md_escape(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\\", "&#92;").replace("|", "&#124;").replace("\r\n", "<br>").replace("\n", "<br>")


def validate_table(c):
    validate_config(c)
    groups, columns = c.get("groups"), c.get("columns")
    if not isinstance(groups, list) or not groups or any(not isinstance(g, dict) for g in groups):
        raise ValueError("groups must be a nonempty list of comparison groups")
    distinct_labels([g.get("id") for g in groups], "comparison group IDs")
    for g in groups:
        methods = g.get("methods")
        if not isinstance(methods, list) or not methods or any(not isinstance(m, dict) for m in methods):
            raise ValueError("Every comparison group needs methods")
        distinct_labels([m.get("id") for m in methods], "method IDs within each group")
        if "rank" in g and type(g["rank"]) is not bool: raise ValueError("rank must be a JSON boolean")
    if not isinstance(columns, list) or not columns or any(not isinstance(col, dict) for col in columns):
        raise ValueError("columns must be a nonempty list")
    seen = set()
    for col in columns:
        if any(not isinstance(col.get(k), str) or not col[k].strip() for k in ("dataset", "metric", "label")):
            raise ValueError("Each column needs dataset, metric and label")
        key = (col["dataset"], col["metric"])
        if key in seen: raise ValueError(f"Duplicate table column: {key}")
        seen.add(key)
        if col.get("direction") not in {"up", "down", "none"}: raise ValueError("Metric direction must be up/down/none")
        if type(col.get("decimals")) is not int or col["decimals"] < 0: raise ValueError("decimals must be a nonnegative integer")
    descriptors = c.get("descriptor_columns", [])
    if descriptors: distinct_labels([d.get("key") for d in descriptors], "descriptor column keys")
    if "column_widths" in c:
        widths = c["column_widths"]
        if len(widths) != 1 + len(descriptors) + len(columns) or any(number(w, "column_width") <= 0 for w in widths):
            raise ValueError("column_widths must provide one positive width per displayed column")


def make_table(config_path,output):
    path=Path(config_path).resolve();c=json.loads(path.read_text(encoding="utf-8"));source=(path.parent/c["data"]).resolve()
    validate_table(c)
    if c["uncertainty"] not in {"sd","none"}:raise ValueError("Uncertainty must be sd or none")
    if not c.get("independent_unit"):raise ValueError("Declare independent unit")
    rows=read_csv(source);keys=["group","method","dataset","metric"]
    unique(rows,[*keys,"run"])
    buckets={}
    for r in rows:buckets.setdefault(tuple(r[k] for k in keys),[]).append(r)
    declared={(g["id"],m["id"],col["dataset"],col["metric"]) for g in c["groups"] for m in g["methods"] for col in c["columns"]}
    extra=set(buckets)-declared
    if extra:raise ValueError(f"Undeclared table cells: {extra}")
    values={};ns={};stats={}
    for key in declared:
        rr=buckets.get(key)
        if not rr:raise ValueError(f"Missing cell {key}: supply status NR/OOM/timeout/error, never silently blank it")
        statuses={r["status"] for r in rr}
        if len(statuses)>1:raise ValueError(f"Mixed successes and failures in {key}; report completion rate separately")
        status=next(iter(statuses))
        if status!="ok":
            if status not in {"NR","OOM","timeout","error","NA"}:raise ValueError(f"Unknown missing status {status}")
            if any(r["value"].strip() for r in rr):raise ValueError("A missing/failed cell cannot also contain a value")
            values[key]=status;ns[key]=0;continue
        s=aggregate(rr,keys,uncertainty=c["uncertainty"])[key];stats[key]=s;ns[key]=s["n"]
        col=next(col for col in c["columns"] if (col["dataset"],col["metric"])==key[2:])
        d=col["decimals"]
        values[key]=f'{s["mean"]:.{d}f}'+(f' ± {s["sd"]:.{d}f}' if c["uncertainty"]=="sd" else "")
    for col in c["columns"]:
        if col["direction"] not in {"up","down","none"}:raise ValueError("Metric direction must be up/down/none")
    ranks={}
    for g in c["groups"]:
        for col in c["columns"]:
            if col["direction"]=="none" or not g.get("rank",True):continue
            kk=[(g["id"],m["id"],col["dataset"],col["metric"]) for m in g["methods"]]
            rounded={k:round(stats[k]["mean"],col["decimals"]) for k in kk if k in stats}
            order=sorted(set(rounded.values()),reverse=col["direction"]=="up")
            for k,v in rounded.items():ranks[k]=order.index(v)+1
    desc=c.get("descriptor_columns",[])
    headers=["Method / variant",*[d["label"] for d in desc],*[f'{col["dataset"]}\n{col["label"]} {dict(up="↑",down="↓",none="")[col["direction"]]}' for col in c["columns"]]]
    body=[];bodymeta=[];group_rows=[]
    for g in c["groups"]:
        group_rows.append(len(body));body.append([g["label"]]+[""]*(len(headers)-1));bodymeta.append(None)
        for m in g["methods"]:
            body.append([m.get("label",m["id"]),*[str(m.get(d["key"],"—")) for d in desc],*[values[(g["id"],m["id"],col["dataset"],col["metric"])] for col in c["columns"]]])
            bodymeta.append((g["id"],m["id"]))
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    with (output/f'{c["id"]}.csv').open("w",encoding="utf-8",newline="") as f:
        wr=csv.writer(f);wr.writerow([h.replace("\n"," / ") for h in headers]);wr.writerows(body)
    caption=c["caption"]+" Bold: best displayed mean within each comparison block; ties at displayed precision are retained. This marking is not a significance test."
    if c["synthetic"]:caption="SYNTHETIC EXAMPLE. "+caption
    md=["| "+" | ".join(md_escape(h.replace("\n"," / ")) for h in headers)+" |","| "+" | ".join(["---"]*len(headers))+" |"]
    tex=[r"% Requires \usepackage{booktabs}. Generated from raw runs; do not edit numbers here.",r"\begin{table*}[t]",r"\centering",r"\caption{"+tex_escape(caption)+"}",r"\label{tab:"+c["id"]+"}",r"\small",r"\begin{tabular}{l"+"c"*(len(headers)-1)+"}",r"\toprule"]
    tex.append(" & ".join(tex_escape(h.replace("\n"," / ")) for h in headers)+r" \\")
    tex.append(r"\midrule")
    for i,row in enumerate(body):
        meta=bodymeta[i]
        if meta is None:
            tex.append(r"\multicolumn{"+str(len(headers))+r"}{l}{\textit{"+tex_escape(row[0])+r"}} \\")
            md.append("| "+" | ".join(md_escape(v) for v in row)+" |");continue
        tr=[];mr=[]
        for j,val in enumerate(row):
            key=(*meta,c["columns"][j-len(desc)-1]["dataset"],c["columns"][j-len(desc)-1]["metric"]) if j>len(desc) else None
            best=key is not None and ranks.get(key)==1
            esc=tex_escape(val);tr.append(r"\textbf{"+esc+"}" if best else esc);mv=md_escape(val);mr.append("**"+mv+"**" if best else mv)
        tex.append(" & ".join(tr)+r" \\");md.append("| "+" | ".join(mr)+" |")
    tex += [r"\bottomrule",r"\end{tabular}",r"\end{table*}"]
    (output/f'{c["id"]}.tex').write_text("\n".join(tex)+"\n",encoding="utf-8")
    (output/f'{c["id"]}.md').write_text("\n".join(md)+"\n\n"+caption+"\n",encoding="utf-8")
    # This display matrix is also the authoritative input to native PowerPoint tables.
    payload={"id":c["id"],"synthetic":c["synthetic"],"headers":headers,"rows":body,"group_rows":group_rows,"caption":caption,
             "column_widths":c.get("column_widths"),
             "best_cells": [[i+1,j+len(desc)+1] for i,meta in enumerate(bodymeta) if meta for j,col in enumerate(c["columns"]) if ranks.get((*meta,col["dataset"],col["metric"]))==1],
             "ranks": {"|".join(k):v for k,v in ranks.items()}, "cells": {"|".join(k):v for k,v in stats.items()}}
    (output/f'{c["id"]}.table.json').write_text(json.dumps(payload,indent=2,ensure_ascii=False),encoding="utf-8")
    style(c);fig,ax=plt.subplots(figsize=(c.get("width_mm",180)/25.4,c.get("height_mm",90)/25.4));ax.axis("off")
    # Column widths are deliberate, with room for method names and error terms.
    widths=c.get("column_widths",[.27]+[.73/(len(headers)-1)]*(len(headers)-1))
    table=ax.table(cellText=body,colLabels=headers,cellLoc="center",colWidths=widths,bbox=[0,.03,1,.9])
    table.auto_set_font_size(False);table.set_fontsize(c.get("font_pt",7))
    for (i,j),cell in table.get_celld().items():
        cell.set_edgecolor("#999999");cell.set_linewidth(.35);cell.visible_edges="B"
        if i==0:cell.set_text_props(weight="bold");cell.set_facecolor("#EEF3F8");cell.visible_edges="TB"
        if j==0:cell.set_text_props(ha="left")
        if i>0 and i-1 in group_rows:cell.set_text_props(weight="bold",color="#0F4D92");cell.set_facecolor("#F2F4F5")
        if i>0 and bodymeta[i-1] and j>len(desc):
            col=c["columns"][j-len(desc)-1];key=(*bodymeta[i-1],col["dataset"],col["metric"])
            if ranks.get(key)==1:cell.set_text_props(weight="bold")
    fig.text(.105,.10,c["short_note"],fontsize=6.5)
    c["kind"]="table"
    audit=finish(fig,c,output,[path,source],{"n_per_cell":{"|".join(k):v for k,v in ns.items()},"rank_policy":"display precision within comparison block; not significance","table_files":[f'{c["id"]}.{e}' for e in ["csv","md","tex","table.json"]]})
    return audit


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("config",type=Path);p.add_argument("--out",type=Path,required=True);a=p.parse_args()
    print(json.dumps(make_table(a.config,a.out),ensure_ascii=False,indent=2))
