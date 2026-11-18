"""Rebuild the explicitly SYNTHETIC teaching data and ready-to-run configurations.

Never point this script at real experiment results. It writes only under assets/examples.
"""
import csv
import json
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"assets/examples"


def save(name,kind,fields,rows,**kw):
    data=BASE/"data"/f"{name}.csv";data.parent.mkdir(parents=True,exist_ok=True)
    with data.open("w",encoding="utf-8",newline="") as f:
        w=csv.writer(f);w.writerow(fields);w.writerows(rows)
    config={"id":name,"kind":kind,"data":f"../data/{name}.csv","synthetic":True,
            "provenance":"Deterministic teaching data from scripts/make_examples.py; not a paper reproduction or research result.",
            "width_mm":180,"height_mm":75,"font_pt":8,"dpi":300,"formats":["svg","pdf","png"],"uncertainty":"none",**kw}
    p=BASE/"configs"/f"{name}.json";p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(config,indent=2,ensure_ascii=False),encoding="utf-8")


def curve_rows(spec):
    out=[]
    for panel,series,xs,ys in spec:
        for x,y in zip(xs,ys):
            for run,offset in enumerate([-.6,.1,.5],1):out.append([panel,series,x,run,round(y+offset,5),"ok"])
    return out


def build():
    BASE.mkdir(parents=True,exist_ok=True);rng=np.random.default_rng(20261118)
    fields=["panel","series","x","run","value","status"]
    save("F01-motivation","curves",fields,curve_rows([
        ("budget","Baseline",[1,2,4,8,16,32],[20,32,43,53,61,67]),("budget","Variant",[1,2,4,8,16,32],[29,39,47,53,57,59]),
        ("noise","Baseline",[0,.1,.3,.5,.8],[76,71,61,47,25]),("noise","Variant",[0,.1,.3,.5,.8],[75,72,65,53,34])]),
        title="Motivating observations under controlled conditions",uncertainty="sd",independent_unit="Independent synthetic run",panels=[
            {"id":"budget","title":"(a) Budget-dependent benefit","series":["Baseline","Variant"],"xlabel":"Sampling budget k (log scale)","ylabel":"Task success (%) ↑","xscale":"log"},
            {"id":"noise","title":"(b) Controlled stress test","series":["Baseline","Variant"],"xlabel":"Injected noise ratio","ylabel":"Task accuracy (%) ↑"}])
    labels=["Full","No reliability","No adaptation","Frozen update"]
    rows=[[s,r,y+[-.5,.1,.4][r-1]+(r-2)*i*.15,"ok"] for i,(s,y) in enumerate(zip(labels,[81,76,78,82])) for r in [1,2,3]]
    save("F04-ablation","ablation",["series","run","value","status"],rows,series=labels,reference="Full",ylabel="Accuracy (%) ↑",delta_label="Full − variant\n(percentage points)",title="Component effects and paired differences",uncertainty="sd",independent_unit="Matched independent seed",height_mm=80)
    rows=[]
    for s,a,b in [("Clean",6,2),("Corrupted",2,5)]:
        rows += [[s,i,float(v)] for i,v in enumerate(rng.beta(a,b,160))]
    save("F05-distribution","distribution",["series","sample_id","value"],rows,series=["Clean","Corrupted"],range=[0,1],bins=16,xlabel="Reliability score",title="Diagnostic distributions",height_mm=75)
    rows=[];panels=[]
    for p,name in enumerate(["Initial","Refined","Reference"]):
        panels.append({"id":name,"title":name,"x_values":list(range(6)),"y_values":list(range(6)),"xlabel":"View B sample","ylabel":"View A sample"})
        for y in range(6):
            for x in range(6):
                same=x//2==y//2
                value=(.8 if x==y else .1) if p==0 else ((.9 if same else .03) if p==2 else (.65 if same else .12))
                rows.append([name,x,y,value,"ok"])
    save("F06-alignment","heatmap",["panel","x","y","value","status"],rows,panels=panels,vmin=0,vmax=1,colorbar="Similarity",annotate=False,title="Matched matrix ordering and a shared colour scale",height_mm=70)
    save("F07-sensitivity-1d","curves",fields,curve_rows([
        ("lambda","Dataset A",[.001,.01,.1,1,10],[66,73,79,80,67]),("lambda","Dataset B",[.001,.01,.1,1,10],[57,63,66,65,52])]),
        panels=[{"id":"lambda","series":["Dataset A","Dataset B"],"xlabel":"Regularization weight (log scale)","ylabel":"Validation accuracy (%) ↑","xscale":"log","default":.1}],title="Parameter range and a declared default",uncertainty="sd",independent_unit="Independent synthetic seed",width_mm=100,height_mm=78)
    rows=[]
    for y in [.1,.3,.5,.7]:
        for x in [.001,.01,.1,1]:
            failed=x==.001 and y==.7
            rows.append(["grid",x,y,"" if failed else round(82-abs(np.log10(x)+1)*2-abs(y-.3)*8,1),"error" if failed else "ok"])
    save("F08-sensitivity-2d","heatmap",["panel","x","y","value","status"],rows,panels=[{"id":"grid","title":"Validation score (%) ↑","x_values":[.001,.01,.1,1],"y_values":[.1,.3,.5,.7],"xlabel":"Weight (discrete tested values)","ylabel":"Threshold (tested values)"}],vmin=65,vmax=85,colorbar="Accuracy (%)",title="Joint parameter grid; failed cells remain visible",width_mm=105,height_mm=82)
    save("F09-robustness","curves",fields,curve_rows([
        (p,s,[0,.2,.5,.8],[start,start-5,start-13,start-29]) for p,start in [("A",83),("B",69)] for s in ["Proposed"]]+[
        (p,s,[0,.2,.5,.8],[start,start-10,start-26,start-42]) for p,start in [("A",84),("B",70)] for s in ["Baseline"]]),
        panels=[{"id":p,"title":"Dataset "+p,"series":["Baseline","Proposed"],"xlabel":"Missing-view ratio","ylabel":"Accuracy (%) ↑"} for p in ["A","B"]],title="Performance across the declared stress range",uncertainty="sd",independent_unit="Independently sampled missingness pattern")
    xs=[0,2,5,10,15,20,30]
    save("F10-convergence","curves",fields,curve_rows([
        ("objective","Solver A",xs,[100,78,60,42,35,33,32]),("objective","Solver B",xs,[100,84,70,57,50,46,45]),
        ("score","Solver A",xs,[40,58,70,76,75,78,77]),("score","Solver B",xs,[40,49,58,65,67,67,68])]),
        panels=[{"id":"objective","series":["Solver A","Solver B"],"xlabel":"Iteration","ylabel":"Objective value ↓","phase":10},
                {"id":"score","series":["Solver A","Solver B"],"xlabel":"Iteration","ylabel":"Task accuracy (%) ↑","phase":10}],title="Optimization progress and task performance",uncertainty="sd",independent_unit="Independent initialization")
    rows=[]
    for s,x,y in [("Small",12,70),("Large",45,82),("Adaptive",24,80),("Control",34,74)]:
        for r,e in enumerate([-.5,0,.5],1):rows.append([s,r,x+e,y+e*.6,"ok"])
    save("F11-efficiency","efficiency",["series","run","cost","score","status"],rows,series=["Small","Large","Adaptive","Control"],xlabel="End-to-end latency (ms) ↓",ylabel="Accuracy (%) ↑",title="Accuracy and measured cost",uncertainty="sd",independent_unit="Independent timing/evaluation run",hardware_protocol="SYNTHETIC: same hypothetical device, batch=1, includes all inference modules; replace with actual protocol",width_mm=115,height_mm=85)
    rows=[[s,f"K{i+1}",v] for s,vs in [("Baseline",[.1,.12,.13,.15,.5]),("Proposed",[.2,.2,.2,.22,.18])] for i,v in enumerate(vs)]
    save("F12-weights","weights",["series","component","value"],rows,series=["Baseline","Proposed"],components=[f"K{i+1}" for i in range(5)],normalized=True,ylabel="Normalized component weight",ymax=.6,title="Internal weights; interpretation needs downstream controls",width_mm=110,height_mm=78)
    rows=[]
    for i in range(90):
        cls=i%3;z=rng.normal(size=2)
        for p,scale in [("Before",.3),("After",2)]:rows.append([p,i,f"Class {cls+1}",float(z[0]+scale*(cls-1)),float(z[1]+scale*(cls%2))])
    save("F13-embedding","embedding",["panel","sample_id","class","x","y"],rows,panels=["Before","After"],classes=["Class 1","Class 2","Class 3"],xlim=[-5,5],ylim=[-4,6],projection_protocol="Synthetic 2D coordinates, no t-SNE or UMAP was run. Real tasks must supply method, fitted sample IDs, seed, parameters and joint/separate-fit policy.",title="The same sample IDs under two representations")
    images=BASE/"images";images.mkdir(exist_ok=True);rows=[]
    for i,case in enumerate(["C01","C02"]):
        for j,method in enumerate(["Input","Baseline","Proposed","Reference"]):
            im=Image.new("RGB",(160,120),(242,244,246));d=ImageDraw.Draw(im)
            d.rectangle([35,30,108,87],fill=(168,205,222));d.ellipse([55,43,90,78],fill=(15,77,146))
            if j==0:d.line([20,70,140,45],fill=(190,180,180),width=10)
            if j==1 or (i==1 and j==2):d.rectangle([70,45,92,70],fill=(238,232,216))
            d.text((5,100),"SYNTHETIC",fill=(90,90,90));fn=f'{case}-{method}.png';im.save(images/fn)
            rows.append([case,method,f"../images/{fn}","improvement" if i==0 else "failure",50,40,45,42])
    save("F14-cases","cases",["case_id","method","path","outcome","roi_x","roi_y","roi_w","roi_h"],rows,methods=["Input","Baseline","Proposed","Reference"],case_ids=["C01","C02"],selection_protocol="Two explicitly synthetic illustrative cases: one improvement and one retained failure. For research replace with predeclared selection and real IDs.",title="Matched images and regions; include a failure",height_mm=100)
    table_examples()


def table_examples():
    cols=[{"dataset":d,"metric":m,"label":m,"direction":di,"decimals":1} for d,m,di in [("Set A","ACC","up"),("Set A","NMI","up"),("Set B","ACC","up"),("Set B","NMI","up")]]
    groups=[{"id":"matched","label":"Matched training and evaluation protocol","methods":[{"id":s} for s in ["Baseline A","Baseline B","Proposed"]]},
            {"id":"extra","label":"Extra supervision (reference only)","rank":False,"methods":[{"id":"Reference+"}]}]
    values=[[74,62,80,68],[77,64,79,70],[79,65,79,69],[84,72,86,75]]
    write_table("T01-main",cols,groups,values,caption="Mean ± sample SD of three independent synthetic runs per available cell. OOM denotes an explicitly failed run configuration. Extra supervision is a separate reference block.",short_note="Synthetic: mean ± SD, n=3. Bold = best displayed mean per block. OOM ≠ 0.")
    cols=[{"dataset":"Matched task","metric":"ACC","label":"ACC","direction":"up","decimals":1},{"dataset":"Matched task","metric":"NMI","label":"NMI","direction":"up","decimals":1}]
    methods=[{"id":s,"R":r,"A":a,"phase":phase} for s,r,a,phase in [("Full","on","on","train+test"),("No reliability","off","on","train+test"),("No adaptation","on","off","train"),("Frozen update","on","on","frozen")]]
    write_table("T02-ablation",cols,[{"id":"controlled","label":"Matched data, seeds and training budget","methods":methods}],[[81,69],[76,63],[78,66],[82,68]],descriptor_columns=[{"key":"R","label":"Reliability"},{"key":"A","label":"Adaptation"},{"key":"phase","label":"Stage"}],column_widths=[.23,.14,.14,.17,.16,.16],caption="Controlled component variants. Mean ± SD over three matched synthetic seeds. Frozen update is an alternative strategy, not a pure component removal.",short_note="Synthetic: mean ± SD, n=3 paired seeds. on/off has an explicit definition.",height_mm=85,font_pt=7)
    cols=[{"dataset":"Validation","metric":"ACC","label":"ACC","direction":"up","decimals":1}]
    methods=[{"id":f"Setting {i+1}","lambda":v,"beta":b,"selected":"default" if i==2 else ""} for i,(v,b) in enumerate([(0.001,.3),(.01,.3),(.1,.3),(1,.3),(.1,.7)])]
    write_table("T03-parameter",cols,[{"id":"search","label":"Validation sweep; test set not used for selection","methods":methods}],[[71],[77],[81],[80],[76]],descriptor_columns=[{"key":"lambda","label":"Weight"},{"key":"beta","label":"Threshold"},{"key":"selected","label":"Selection"}],column_widths=[.25,.18,.18,.19,.2],caption="Mean ± sample SD over three independent synthetic runs. One- and two-factor settings are explicitly enumerated. Default is selected on validation data; this example does not establish a real optimal setting.",short_note="Synthetic: mean ± SD, n=3. State tested values, selection split and fixed settings.",height_mm=90,font_pt=7)
    cols=[{"dataset":"Inference","metric":"ACC","label":"ACC (%)","direction":"up","decimals":1},{"dataset":"Inference","metric":"latency","label":"Latency (ms)","direction":"down","decimals":1},{"dataset":"Inference","metric":"memory","label":"Memory (GB)","direction":"down","decimals":1}]
    write_table("T04-efficiency",cols,[{"id":"device","label":"Same device / batch / precision / input / timing scope","methods":[{"id":s} for s in ["Small","Large","Adaptive"]]}],[[70,12,2],[82,45,6],[80,24,3]],caption="Synthetic means and SD over three independent runs. Latency includes preprocessing, model and postprocessing; memory denotes peak allocation. No real hardware was measured.",short_note="Synthetic: mean ± SD, n=3. Accuracy ↑; latency and memory ↓. End-to-end scope.",height_mm=75,font_pt=7)


def write_table(name,cols,groups,values,**kw):
    rows=[];i=0
    for g in groups:
        for m in g["methods"]:
            for j,col in enumerate(cols):
                if name=="T01-main" and m["id"]=="Baseline A" and col["dataset"]=="Set B":rows.append([g["id"],m["id"],col["dataset"],col["metric"],"failed","","OOM"]);continue
                for r,e in enumerate([-.3,0,.3],1):rows.append([g["id"],m["id"],col["dataset"],col["metric"],r,round(values[i][j]+e,5),"ok"])
            i+=1
    save(name,"table",["group","method","dataset","metric","run","value","status"],rows,columns=cols,groups=groups,uncertainty="sd",independent_unit="Independent synthetic seed/run",title=name.replace("-"," "),**kw)


if __name__=="__main__":
    build();print(f"Synthetic examples written under {BASE}")
