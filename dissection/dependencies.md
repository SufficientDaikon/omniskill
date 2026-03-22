# Dependencies

## Critical Issue: Undeclared Runtime Dependencies

The `pyproject.toml` declares **zero runtime dependencies** under `[project.dependencies]` (the field is absent entirely). However, the codebase requires 4 third-party packages:

| Package | PyPI Name | Usage | Import Locations |
|---------|-----------|-------|-----------------|
| **typer** | typer | CLI framework | cli.py, all 16 command modules |
| **rich** | rich | Console output, tables, progress | utils/output.py |
| **pyyaml** | PyYAML | YAML parsing | 15+ core modules |
| **platformdirs** | platformdirs | Path resolution | utils/paths.py |

**This means `pip install omniskill` will succeed but `omniskill` CLI will crash on first use with `ModuleNotFoundError`.**

## Build Dependencies

| Package | Purpose | Declared |
|---------|---------|----------|
| hatchling | Build backend | Yes (in `[build-system].requires`) |

**Issue:** `pyproject.toml` originally had `build-backend = "hatchling.backends"` (wrong module path). Fixed to `"hatchling.build"` during this dissection.

## Dev Dependencies

| Package | Purpose | Declared |
|---------|---------|----------|
| pytest | Test runner | No (not declared anywhere) |

## Standard Library Usage

Heavily used stdlib modules (no installation needed):
- `pathlib` — Path manipulation
- `json` — State persistence
- `dataclasses` — Data modeling
- `enum` — Status enumerations
- `uuid` — ID generation
- `datetime` — Timestamps
- `re` — Regex for validation
- `hashlib` — SHA-256 checksums
- `importlib.util` — Dynamic hook loading
- `xml.etree.ElementTree` — Prompt library parsing
- `glob` — Artifact pattern matching
- `time` — Duration measurement

## Dependency Graph

```
omniskill
├── typer (>=0.24)
│   ├── click (>=8.2)
│   │   └── colorama (Windows)
│   ├── shellingham
│   └── annotated-doc
├── rich (>=14)
│   ├── markdown-it-py
│   │   └── mdurl
│   └── pygments
├── PyYAML (>=6.0)
└── platformdirs (>=4.0)
```

## Recommended Fix

Add to `pyproject.toml`:
```toml
[project]
dependencies = [
    "typer>=0.12",
    "rich>=13",
    "PyYAML>=6.0",
    "platformdirs>=4.0",
]

[project.optional-dependencies]
dev = ["pytest>=8.0"]

[project.scripts]
omniskill = "omniskill.cli:app"
```

The `[project.scripts]` entry is also missing — the CLI only works via `python -m omniskill`, not as a standalone `omniskill` command.
