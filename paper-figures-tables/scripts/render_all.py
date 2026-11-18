"""Render all bundled synthetic examples without modifying their inputs."""
import argparse
import json
from pathlib import Path
from figurekit import render
from tablekit import make_table

ROOT=Path(__file__).resolve().parents[1]
if __name__=="__main__":
    p=argparse.ArgumentParser();p.add_argument("--out",type=Path,default=ROOT/"assets/gallery");a=p.parse_args()
    for c in sorted((ROOT/"assets/examples/configs").glob("*.json")):
        spec=json.loads(c.read_text(encoding="utf-8"))
        result=make_table(c,a.out) if spec["kind"]=="table" else render(c,a.out)
        print(result["id"])
