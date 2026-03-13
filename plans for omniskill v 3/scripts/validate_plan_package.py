import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def parse_xml(path: Path):
    ET.parse(path)


def validate_index_xsd(index_path: Path, xsd_path: Path) -> tuple[bool, str]:
    try:
        import xmlschema  # type: ignore
    except Exception:
        return False, "xmlschema package is missing"
    try:
        schema = xmlschema.XMLSchema(str(xsd_path))
        schema.validate(str(index_path))
        return True, "ok"
    except Exception as e:
        return False, str(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True)
    parser.add_argument("--xsd", required=True)
    args = parser.parse_args()

    root = Path(args.dir)
    files = sorted(root.glob("*.xml"))
    report = {"xml_files": len(files), "well_formed": [], "errors": []}

    for f in files:
        try:
            parse_xml(f)
            report["well_formed"].append(f.name)
        except Exception as e:
            report["errors"].append({"file": f.name, "error": str(e)})

    ok, msg = validate_index_xsd(root / "00-plan-index.xml", Path(args.xsd))
    report["xsd_index_validation"] = {"ok": ok, "message": msg}

    print(json.dumps(report, indent=2))
    if report["errors"] or not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
