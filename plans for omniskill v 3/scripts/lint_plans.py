import argparse
import json
import re
from pathlib import Path
import xml.etree.ElementTree as ET


def txt(node, default=""):
    return (node.text or default).strip() if node is not None else default


def lint_prompt_library(path: Path):
    issues = []
    tree = ET.parse(path)
    root = tree.getroot()

    req = {"context", "role", "objective", "instructions", "steps", "do", "dont", "evidence", "response_format"}
    prompts = root.findall("prompt")

    for p in prompts:
        pid = p.attrib.get("id", "unknown")
        present = {c.tag for c in list(p)}
        missing = sorted(req - present)
        if missing:
            issues.append(f"{pid}: missing fields {', '.join(missing)}")

        do_text = txt(p.find("do")).lower()
        dont_text = txt(p.find("dont")).lower()
        overlap = set(re.findall(r"[a-z_]{4,}", do_text)) & set(re.findall(r"[a-z_]{4,}", dont_text))
        noisy = {w for w in overlap if w not in {"with", "from", "that", "this", "where", "must", "evidence", "policy"}}
        if len(noisy) > 6:
            issues.append(f"{pid}: potential do/dont contradiction; high token overlap")

    return issues


def lint_baseline_directive(index_path: Path):
    text = index_path.read_text(encoding="utf-8")
    if "OMNISKILL v2 as the mandatory implementation baseline" not in text:
        return ["index: missing OMNISKILL v2 baseline directive"]
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    args = ap.parse_args()

    root = Path(args.dir)
    issues = []

    required = [f"{i:02d}-" for i in range(0, 29)]
    names = [p.name for p in root.glob("*.xml")]
    for pref in required:
        if not any(n.startswith(pref) for n in names):
            issues.append(f"missing required plan file prefix: {pref}")

    issues += lint_baseline_directive(root / "00-plan-index.xml")
    issues += lint_prompt_library(root / "10-claude-prompt-library.xml")

    report = {"issue_count": len(issues), "issues": issues}
    print(json.dumps(report, indent=2))
    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

