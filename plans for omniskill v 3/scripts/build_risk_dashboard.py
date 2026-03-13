import argparse
import json
from pathlib import Path


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--snapshots", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    snaps = load(Path(args.snapshots))
    labels = [s["iteration"] for s in snaps]
    risks = [s["risk_score"] for s in snaps]

    rows = "\n".join([f"<tr><td>{s['iteration']}</td><td>{s['risk_score']}</td><td>{s['notes']}</td></tr>" for s in snaps])

    html = f"""<!doctype html>
<html><head><meta charset='utf-8'><title>Risk Burndown</title>
<style>body{{font-family:Segoe UI,Arial;padding:24px}}table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ddd;padding:8px}}</style>
</head><body>
<h1>OMNISKILL v3 Risk Burndown</h1>
<canvas id='c' width='900' height='320'></canvas>
<p>Lower is better. Source: execution gate snapshots.</p>
<table><thead><tr><th>Iteration</th><th>Risk Score</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table>
<script>
const labels = {json.dumps(labels)};
const vals = {json.dumps(risks)};
const cv = document.getElementById('c'); const ctx = cv.getContext('2d');
ctx.clearRect(0,0,cv.width,cv.height); ctx.beginPath(); ctx.strokeStyle='#2563eb'; ctx.lineWidth=2;
const max = Math.max(...vals, 100), min = 0; const left=50,right=20,top=20,bottom=40;
for(let i=0;i<vals.length;i++){{
  const x = left + (i*(cv.width-left-right)/(Math.max(vals.length-1,1)));
  const y = top + ((max-vals[i])*(cv.height-top-bottom)/(max-min));
  if(i===0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
  ctx.fillStyle='#111'; ctx.fillText(labels[i], x-12, cv.height-10);
}}
ctx.stroke();
</script>
</body></html>"""

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(json.dumps({"written": str(out), "points": len(snaps)}, indent=2))


if __name__ == "__main__":
    main()
