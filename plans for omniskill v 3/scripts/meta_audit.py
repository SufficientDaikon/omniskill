import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()
    root = Path(args.dir)

    report = {"missing": [], "checks": []}

    files = sorted([p.name for p in root.glob("*.xml")])
    for i in range(0, 29):
        pref = f"{i:02d}-"
        if not any(n.startswith(pref) for n in files):
            report["missing"].append(pref)

    # index coverage check
    idx = ET.parse(root / "00-plan-index.xml").getroot()
    indexed = {d.attrib.get("file", "") for d in idx.findall("documents/document")}
    for n in files:
        if n != "00-plan-index.xml" and n not in indexed:
            report["checks"].append(f"index missing document reference: {n}")

    # key directives
    txt = (root / "08-claude-execution-playbook.xml").read_text(encoding="utf-8")
    for phrase in [
        "OMNISKILL v2 as the execution substrate",
        "toolUsageEnforcement",
        "contextFloodPrevention",
    ]:
        if phrase not in txt:
            report["checks"].append(f"playbook missing phrase: {phrase}")

    ok = not report["missing"] and not report["checks"]
    report["ok"] = ok
    print(json.dumps(report, indent=2))
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
