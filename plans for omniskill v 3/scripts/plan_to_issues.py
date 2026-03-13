import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def parse_backlog(path: Path):
    root = ET.parse(path).getroot()
    epics = []
    for e in root.findall("epic"):
        epics.append({
            "id": e.attrib.get("id", ""),
            "name": e.attrib.get("name", ""),
            "priority": e.attrib.get("priority", "P1"),
            "dependsOn": (e.findtext("dependsOn") or "").strip(),
            "stories": [s.text.strip() for s in e.findall("stories/story") if s.text],
            "dod": [d.text.strip() for d in e.findall("definitionOfDone/item") if d.text],
        })
    return epics


def to_issue_markdown(epic):
    deps = epic["dependsOn"] if epic["dependsOn"] else "None"
    stories = "\n".join([f"- [ ] {s}" for s in epic["stories"]])
    dod = "\n".join([f"- [ ] {d}" for d in epic["dod"]])
    return f"""# {epic['id']} - {epic['name']}

## Priority
`{epic['priority']}`

## Dependencies
{deps}

## Stories
{stories}

## Definition of Done
{dod}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backlog", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    epics = parse_backlog(Path(args.backlog))

    issue_index = []
    for epic in epics:
        fname = f"{epic['id']}-{epic['name'].lower().replace(' ', '-')}.md"
        path = out / fname
        path.write_text(to_issue_markdown(epic), encoding="utf-8")
        issue_index.append({"epic": epic["id"], "title": epic["name"], "file": fname, "priority": epic["priority"]})

    (out / "issues.json").write_text(json.dumps(issue_index, indent=2), encoding="utf-8")
    print(json.dumps({"generated": len(issue_index), "out": str(out)}, indent=2))


if __name__ == "__main__":
    main()
