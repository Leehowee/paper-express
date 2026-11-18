"""Data-driven paper figures. Style adapted from figures4papers; see THIRD_PARTY.md.

Every example is synthetic. Real tasks must supply their own data and provenance.
Only the Python standard library, NumPy, Matplotlib and Pillow are required.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import math
import os
import platform
import re
import textwrap
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

COLORS = ["#0F4D92", "#42949E", "#9A4D8E", "#B64342", "#777777", "#AF8200"]
MARKERS = ["o", "s", "^", "D", "v", "P"]
LINES = ["-", "--", "-.", ":", "--", "-."]


def read_csv(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, strict=True)
        fields = reader.fieldnames
        if not fields or any(not field.strip() for field in fields):
            raise ValueError("CSV needs nonempty column names")
        if len(fields) != len(set(fields)):
            raise ValueError("Duplicate CSV column names would overwrite data")
        rows = []
        try:
            for row in reader:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError(f"CSV row ending at line {reader.line_num} has the wrong number of fields")
                rows.append(row)
        except csv.Error as exc:
            raise ValueError(f"Malformed CSV near line {reader.line_num}: {exc}") from exc
        return rows


def distinct_labels(values, field):
    if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
        raise ValueError(f"{field}: use a nonempty list of nonempty labels")
    if len(values) != len(set(values)):
        raise ValueError(f"{field}: duplicate labels would repeat observations or display cells")


def validate_config(c):
    if type(c.get("synthetic")) is not bool:
        raise ValueError("synthetic must be the JSON boolean true or false, not a string")
    if not isinstance(c.get("provenance"), str) or not c["provenance"].strip():
        raise ValueError("Declare nonempty provenance")
    if not isinstance(c.get("id"), str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", c["id"]):
        raise ValueError("id must be a filename-safe identifier without a directory path")
    for field in ("width_mm", "height_mm", "font_pt", "dpi"):
        if field in c and (type(c[field]) not in (int, float) or number(c[field], field) <= 0):
            raise ValueError(f"{field} must be a positive number")
    formats = c.get("formats", ["svg", "pdf", "png"])
    distinct_labels(formats, "formats")
    if set(formats) - {"svg", "pdf", "png"}:
        raise ValueError("Supported formats: svg, pdf, png")
    for key in ("series", "classes", "components", "methods", "case_ids"):
        if key in c:
            distinct_labels(c[key], key)
    if "panels" in c:
        panels = c["panels"]
        if not isinstance(panels, list) or not panels:
            raise ValueError("panels must be a nonempty list")
        if all(isinstance(p, dict) for p in panels):
            distinct_labels([p.get("id") for p in panels], "panel IDs")
            for p in panels:
                if "series" in p: distinct_labels(p["series"], "panel series")
                for axis in ("x_values", "y_values"):
                    if axis in p:
                        if not isinstance(p[axis], list) or not p[axis]: raise ValueError(f"{axis} must be nonempty")
                        vals = [number(v, axis) for v in p[axis]]
                        if len(vals) != len(set(vals)): raise ValueError(f"Duplicate {axis} coordinates")
        else:
            distinct_labels(panels, "panels")


def number(value, field):
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field}: expected a finite number, got {value!r}") from exc
    if not math.isfinite(result):
        raise ValueError(f"{field}: NaN/Inf are not valid measurements; use status")
    return result


def unique(rows, fields):
    seen = set()
    for r in rows:
        if any(k not in r or r[k] is None or not str(r[k]).strip() for k in fields):
            raise ValueError(f"Observation IDs must be present and nonempty: {fields}")
        key = tuple(r[k] for k in fields)
        if key in seen:
            raise ValueError(f"Duplicate independent observation: {fields}={key}")
        seen.add(key)


def aggregate(rows, fields, value="value", uncertainty="sd"):
    """Aggregate independent runs, never pool different conditions or missing cells."""
    if uncertainty not in {"sd", "none"}:
        raise ValueError("Supported uncertainty: sd or none. Supply audited CI separately.")
    unique(rows, [*fields, "run"])
    groups = defaultdict(list)
    for r in rows:
        status = r.get("status", "ok")
        if status != "ok":
            raise ValueError("Raw repeated measurements must all be ok; report failed runs explicitly, do not drop them")
        groups[tuple(r[k] for k in fields)].append(number(r[value], value))
    out = {}
    for key, values in groups.items():
        if uncertainty == "sd" and len(values) < 2:
            raise ValueError(f"{key}: SD requires at least two independent runs")
        with np.errstate(over="ignore", invalid="ignore"):
            mean = float(np.mean(values))
            sd = float(np.std(values, ddof=1)) if len(values) > 1 else None
        if not math.isfinite(mean) or (sd is not None and not math.isfinite(sd)):
            raise ValueError(f"{key}: numerical overflow in mean/SD; rescale the measurements explicitly")
        out[key] = {"mean": mean, "sd": sd, "n": len(values)}
    return out


def style(config):
    plt.rcParams.update({
        "font.family": config.get("font", "DejaVu Sans"),
        "font.size": config.get("font_pt", 8), "axes.labelsize": config.get("font_pt", 8),
        "axes.titlesize": config.get("font_pt", 8), "legend.fontsize": 7,
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.linewidth": .7, "lines.linewidth": 1.3, "lines.markersize": 3.5,
        "xtick.major.width": .7, "ytick.major.width": .7,
        "legend.frameon": False, "svg.fonttype": "none", "pdf.fonttype": 42,
        "savefig.facecolor": "white", "figure.facecolor": "white",
    })


def new_figure(c, rows=1, cols=1):
    return plt.subplots(rows, cols, figsize=(c.get("width_mm", 180)/25.4, c.get("height_mm", 70)/25.4), squeeze=False)


def source_key(source, output):
    source, output = Path(source).resolve(), Path(output).resolve()
    try:
        return os.path.relpath(source, output).replace("\\", "/")
    except ValueError:
        # Windows cannot express a relative path across drive letters.
        return source.as_posix()


def finish(fig, c, output, sources, summary=None):
    if c.get("synthetic", False):
        fig.text(.01, .012, "SYNTHETIC EXAMPLE — replace data before use", fontsize=6, color="#666666")
    if c.get("title"):
        title=textwrap.fill(c["title"],width=max(30,int(c.get("width_mm",180)/2.15)))
        fig.suptitle(title, x=.035, ha="left", fontsize=9, fontweight="bold",y=.98)
    if c["kind"]=="table":
        fig.subplots_adjust(left=.035,right=.98,bottom=.24,top=.86)
    else:
        fig.tight_layout(rect=(.015,.10,.985,.89),pad=.65,w_pad=1.7,h_pad=1.6)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    files = []
    # Do not use bbox_inches='tight': the physical page dimensions are contractual.
    for ext in c.get("formats", ["svg", "pdf", "png"]):
        if ext not in {"svg", "pdf", "png"}:
            raise ValueError(f"Unsupported format {ext}")
        p = output / f'{c["id"]}.{ext}'
        fig.savefig(p, dpi=c.get("dpi", 300))
        files.append(p.name)
    plt.close(fig)
    audit = {"id": c["id"], "kind": c["kind"], "synthetic": c.get("synthetic", False),
             "size_mm": [c.get("width_mm", 180), c.get("height_mm", 70)],
             "uncertainty": c.get("uncertainty", "none"), "independent_unit": c.get("independent_unit"),
             "source_path_base": "audit_directory",
             "source_path_policy": "relative where possible; absolute across drives",
             "source_sha256": {source_key(p, output): hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in sources},
             "outputs": files, "summary": summary or {}, "visual_review": "required"}
    generator_files = [Path(__file__).resolve()]
    if c["kind"] == "table": generator_files.append(Path(__file__).with_name("tablekit.py").resolve())
    audit["generator_sha256"] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in generator_files}
    audit["runtime"] = {"python": platform.python_version(), "numpy": np.__version__, "matplotlib": matplotlib.__version__}
    (output / f'{c["id"]}.audit.json').write_text(json.dumps(audit, indent=2, ensure_ascii=False), encoding="utf-8")
    return audit


def curves(c, data):
    data=[{**r,"x":format(number(r["x"],"x"),".17g")} for r in data]
    panels = c["panels"]
    declared={(p["id"],s) for p in panels for s in p["series"]}
    if {(r["panel"],r["series"]) for r in data} != declared:
        raise ValueError("Curve data and declared panel/series must match exactly")
    fig, axes = new_figure(c, 1, len(panels))
    stats = aggregate(data, ["panel", "series", "x"], uncertainty=c["uncertainty"])
    for ax, p in zip(axes[0], panels):
        series = p["series"]
        for i, label in enumerate(series):
            keys = [k for k in stats if k[0] == p["id"] and k[1] == label]
            keys.sort(key=lambda k: number(k[2], "x"))
            if not keys:
                raise ValueError(f"No data for {p['id']}/{label}")
            xs = [number(k[2], "x") for k in keys]
            ys = [stats[k]["mean"] for k in keys]
            if p.get("xscale", "linear") == "log" and min(xs) <= 0:
                raise ValueError("Log x requires positive values; show zero in a separate ablation")
            sd = [stats[k]["sd"] for k in keys] if c["uncertainty"] == "sd" else None
            ax.errorbar(xs, ys, yerr=sd, color=COLORS[i], marker=MARKERS[i], linestyle=LINES[i], capsize=2, label=label)
        ax.set(xlabel=p["xlabel"], ylabel=p["ylabel"], title=p.get("title", ""))
        ax.set_xscale(p.get("xscale", "linear"))
        if "ylim" in p: ax.set_ylim(p["ylim"])
        if "default" in p: ax.axvline(p["default"], color="#777777", ls=":", lw=.8, label="Default")
        if "phase" in p: ax.axvline(p["phase"], color="#777777", ls=":", lw=.8, label="Phase change")
        ax.grid(axis="y", alpha=.18)
        ax.legend(loc="best")
    return fig, {"groups": len(stats), "n_range": [min(s["n"] for s in stats.values()), max(s["n"] for s in stats.values())]}


def ablation(c, data):
    unique(data, ["series", "run"])
    stats = aggregate(data, ["series"], uncertainty=c["uncertainty"])
    labels = c["series"]
    full = {r["run"]: number(r["value"], "value") for r in data if r["series"] == c["reference"]}
    fig, axes = new_figure(c, 1, 2)
    summaries = {}
    for i, label in enumerate(labels):
        s = stats[(label,)]
        axes[0,0].errorbar(s["mean"], i, xerr=s["sd"] if c["uncertainty"] == "sd" else None, color=COLORS[0] if label == c["reference"] else COLORS[4], fmt="o", capsize=3)
        r = {r["run"]: number(r["value"], "value") for r in data if r["series"] == label}
        if set(r) != set(full):
            raise ValueError("Paired deltas require exactly matched run IDs; no silent intersection")
        delta = [full[k] - r[k] for k in full]
        mean, sd = float(np.mean(delta)), float(np.std(delta, ddof=1)) if len(delta) > 1 else None
        axes[0,1].errorbar(mean, i, xerr=sd if c["uncertainty"] == "sd" else None, fmt="o", color=COLORS[0], capsize=3)
        summaries[label] = {"mean": s["mean"], "delta_full_minus_variant": mean, "paired_sd": sd, "n": len(delta)}
    for ax in axes[0]:
        ax.set_yticks(range(len(labels)), labels); ax.invert_yaxis(); ax.grid(axis="x", alpha=.18)
    axes[0,0].set_xlabel(c["ylabel"])
    axes[0,1].axvline(0, color="#555555", lw=.7)
    axes[0,1].set_xlabel(c.get("delta_label", "Full − variant\n(original metric units)"))
    return fig, summaries


def heatmap(c, data):
    data=[{**r,"x":format(number(r["x"],"x"),".17g"),"y":format(number(r["y"],"y"),".17g")} for r in data]
    panels = c["panels"]
    declared={(p["id"],float(x),float(y)) for p in panels for x in p["x_values"] for y in p["y_values"]}
    observed={(r["panel"],number(r["x"],"x"),number(r["y"],"y")) for r in data}
    if observed != declared: raise ValueError("Every heatmap cell must be declared, including explicit missing/failed status")
    fig, axes = new_figure(c, 1, len(panels))
    unique(data, ["panel", "x", "y"])
    cm = plt.get_cmap("Blues").copy(); cm.set_bad("#E5E5E5")
    for ax, p in zip(axes[0], panels):
        xs, ys = p["x_values"], p["y_values"]
        array = np.full((len(ys), len(xs)), np.nan)
        for r in [r for r in data if r["panel"] == p["id"]]:
            x, y = number(r["x"], "x"), number(r["y"], "y")
            if x not in xs or y not in ys: raise ValueError("Undeclared heatmap coordinate")
            if r.get("status", "ok") == "ok": array[ys.index(y), xs.index(x)] = number(r["value"], "value")
            elif r.get("status") not in {"NR","OOM","timeout","error","NA"}: raise ValueError("Unknown heatmap status")
            elif r["value"].strip(): raise ValueError("Failed/missing cell must have an empty numeric value")
        im = ax.imshow(array, cmap=cm, vmin=c["vmin"], vmax=c["vmax"], interpolation="nearest", aspect="auto")
        ax.set(xticks=range(len(xs)), xticklabels=p.get("x_labels", xs), yticks=range(len(ys)), yticklabels=p.get("y_labels", ys), xlabel=p["xlabel"], ylabel=p["ylabel"], title=p["title"])
        for (y,x), v in np.ndenumerate(array):
            label = "NA" if np.isnan(v) else f'{v:.{c.get("decimals", 1)}f}'
            if c.get("annotate", True): ax.text(x, y, label, ha="center", va="center", fontsize=6.5, color="white" if v > (c["vmin"]+c["vmax"])/2 else "#222222")
        bar=fig.colorbar(im, ax=ax, fraction=.045, pad=.03, label=c["colorbar"] if len(panels)==1 else "")
        bar.ax.tick_params(labelsize=6)
        if len(panels)>1 and p is not panels[0]:ax.set_ylabel("")
    return fig, {"spacing": "categorical grid; axis labels state actual values", "interpolation": "none", "missing": "NA / grey", "missing_cells": [{k:r[k] for k in ["panel","x","y","status"]} for r in data if r.get("status","ok")!="ok"], "colorbar_quantity": c["colorbar"]}


def distribution(c, data):
    unique(data, ["series", "sample_id"])
    fig, axes = new_figure(c, 1, 2)
    bins = np.linspace(c["range"][0], c["range"][1], c["bins"]+1)
    counts = {}
    for i,label in enumerate(c["series"]):
        values = np.array([number(r["value"], "value") for r in data if r["series"] == label])
        if not len(values): raise ValueError("Empty sample group")
        if np.any((values < bins[0]) | (values > bins[-1])): raise ValueError("Histogram range excludes samples")
        axes[0,0].hist(values, bins=bins, density=True, histtype="step", color=COLORS[i], linestyle=LINES[i], label=label)
        xs = np.sort(values); axes[0,1].step(xs, np.arange(1,len(xs)+1)/len(xs), where="post", color=COLORS[i], linestyle=LINES[i], label=label)
        counts[label] = len(values)
    for ax in axes[0]: ax.set_xlabel(c["xlabel"]); ax.legend(loc="upper left",bbox_to_anchor=(0,1.18),ncol=2); ax.grid(alpha=.15)
    axes[0,0].set_ylabel("Probability density"); axes[0,1].set_ylabel("Empirical CDF")
    return fig, {"samples_per_group": counts, "bins": bins.tolist(), "density_area": 1}


def embedding(c, data):
    unique(data, ["panel", "sample_id"])
    labels={}
    for r in data: labels.setdefault(r["sample_id"],set()).add(r["class"])
    if any(len(v)!=1 for v in labels.values()): raise ValueError("Class meaning must remain consistent for each sample ID across panels")
    fig, axes = new_figure(c, 1, len(c["panels"]))
    ids = []
    for ax,p in zip(axes[0],c["panels"]):
        rows = [r for r in data if r["panel"] == p]
        ids.append({r["sample_id"] for r in rows})
        for i, label in enumerate(c["classes"]):
            rr = [r for r in rows if r["class"] == label]
            ax.scatter([number(r["x"],"x") for r in rr], [number(r["y"],"y") for r in rr], s=10, alpha=.65, color=COLORS[i], marker=MARKERS[i], label=label, edgecolors="none")
        ax.set(title=p, xlabel="Projection 1", ylabel="Projection 2", xlim=c["xlim"], ylim=c["ylim"]); ax.legend()
    if any(i != ids[0] for i in ids): raise ValueError("Embedding panels must use the same sample IDs")
    return fig, {"projection_protocol": c["projection_protocol"], "sample_count": len(ids[0]), "not_evidence_of": "causal mechanism or generalization"}


def pareto_flags(points):
    return [not any((x2 <= x and y2 >= y) and (x2 < x or y2 > y) for x2,y2 in points) for x,y in points]


def efficiency(c, data):
    unique(data, ["series", "run"])
    ss = aggregate(data, ["series"], value="score", uncertainty=c["uncertainty"])
    cs = aggregate(data, ["series"], value="cost", uncertainty=c["uncertainty"])
    labels = c["series"]; points = [(cs[(s,)]["mean"],ss[(s,)]["mean"]) for s in labels]
    flags = pareto_flags(points)
    fig,axes = new_figure(c); ax=axes[0,0]
    for i,(s,(x,y),flag) in enumerate(zip(labels,points,flags)):
        if x <= 0: raise ValueError("Cost must be positive")
        ax.errorbar(x,y,xerr=cs[(s,)]["sd"] if c["uncertainty"]=="sd" else None,yerr=ss[(s,)]["sd"] if c["uncertainty"]=="sd" else None,fmt=MARKERS[i],color=COLORS[i],capsize=2,label=s)
        ax.annotate(s,(x,y),xytext=(4,5),textcoords="offset points",fontsize=7)
    frontier=sorted(p for p,f in zip(points,flags) if f)
    ax.plot([p[0] for p in frontier],[p[1] for p in frontier],"--",color="#777777",lw=.8,label="Empirical frontier")
    ax.set(xlabel=c["xlabel"],ylabel=c["ylabel"]);ax.grid(alpha=.18)
    return fig,{"frontier_on_means_only": [s for s,f in zip(labels,flags) if f], "hardware_protocol": c["hardware_protocol"]}


def weights(c, data):
    unique(data,["series","component"])
    fig,axes=new_figure(c);ax=axes[0,0]
    labels=c["components"];width=.8/len(c["series"])
    for i,s in enumerate(c["series"]):
        lookup={r["component"]:number(r["value"],"weight") for r in data if r["series"]==s}
        if set(lookup)!=set(labels):raise ValueError("Missing weight component")
        vals=[lookup[k] for k in labels]
        if min(vals)<0:raise ValueError("Expected nonnegative weights")
        if c.get("normalized") and not math.isclose(sum(vals),1,abs_tol=1e-6):raise ValueError("Normalized weights must sum to one")
        ax.bar(np.arange(len(labels))+(i-(len(c["series"])-1)/2)*width, vals, width, color=COLORS[i],edgecolor="#333333",linewidth=.5,hatch=["", "//", ".."][i%3],label=s)
    ax.set(xticks=range(len(labels)),xticklabels=labels,ylabel=c["ylabel"],ylim=(0,c.get("ymax",1)));ax.legend();ax.grid(axis="y",alpha=.15)
    return fig,{"normalization": "sum to 1" if c.get("normalized") else "as supplied"}


def cases(c, data, base):
    unique(data,["case_id","method"])
    methods=c["methods"];ids=c["case_ids"]
    if {(r["case_id"],r["method"]) for r in data}!={(i,m) for i in ids for m in methods}:raise ValueError("Case data must match the declared case/method grid")
    fig,axes=new_figure(c,len(ids),len(methods))
    sources=[]
    lookup={(r["case_id"],r["method"]):r for r in data}
    for i,case_id in enumerate(ids):
        shapes=set(); rois=set()
        for j,method in enumerate(methods):
            r=lookup[(case_id,method)];p=(base/r["path"]).resolve();sources.append(p)
            im=Image.open(p).convert("RGB");shapes.add(im.size)
            ax=axes[i,j];ax.imshow(im);ax.set_xticks([]);ax.set_yticks([])
            if i==0:ax.set_title(method)
            if j==0:ax.set_ylabel(f'{case_id}\n{r["outcome"]}',fontsize=7)
            roi=tuple(number(r[k],k) for k in ["roi_x","roi_y","roi_w","roi_h"]);rois.add(roi)
            x,y,w,h=roi
            if min(x,y)<0 or min(w,h)<=0 or x+w>im.width or y+h>im.height:raise ValueError("ROI outside image")
            ax.add_patch(plt.Rectangle((x,y),w,h,fill=False,color="#B64342",lw=1))
        if len(shapes)!=1 or len(rois)!=1:raise ValueError("Case panels require aligned image dimensions and the same ROI")
    return fig,{"selection_protocol":c["selection_protocol"],"cases":ids},sources


def render(config_path, output):
    config_path=Path(config_path).resolve();c=json.loads(config_path.read_text(encoding="utf-8"));base=config_path.parent
    validate_config(c)
    if c["kind"] in {"curves","ablation","efficiency"} and not c.get("independent_unit"):raise ValueError("Declare independent experimental unit")
    style(c);path=(base/c["data"]).resolve();data=read_csv(path);sources=[config_path,path]
    if not data: raise ValueError("Input data is empty")
    if c["kind"] in {"ablation","distribution","efficiency","weights"}:
        if set(c["series"]) != {r["series"] for r in data}: raise ValueError("Declared series must match data exactly")
    if c["kind"] == "embedding":
        if set(c["panels"]) != {r["panel"] for r in data} or set(c["classes"]) != {r["class"] for r in data}: raise ValueError("Declared embedding panels/classes must match data")
    series_counts=[len(c.get("series",[])),len(c.get("classes",[]))]+[len(p.get("series",[])) for p in c.get("panels",[]) if isinstance(p,dict)]
    if max(series_counts)>len(COLORS): raise ValueError("This compact template supports at most six series; split panels or extend encodings explicitly")
    handlers={"curves":curves,"ablation":ablation,"heatmap":heatmap,"distribution":distribution,"embedding":embedding,"efficiency":efficiency,"weights":weights}
    if c["kind"]=="cases":fig,summary,more=cases(c,data,base);sources+=more
    elif c["kind"] in handlers:fig,summary=handlers[c["kind"]](c,data)
    else:raise ValueError(f'Unknown figure kind {c["kind"]}')
    return finish(fig,c,output,sources,summary)


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument("config",type=Path);parser.add_argument("--out",type=Path,required=True)
    a=parser.parse_args();print(json.dumps(render(a.config,a.out),ensure_ascii=False,indent=2))
