# Build System

## Build Configuration

| Aspect | Value |
|--------|-------|
| **Build backend** | hatchling 1.29.0 |
| **Package format** | PEP 517/518 via pyproject.toml |
| **Source layout** | `src/omniskill/` (src-layout) |
| **Version** | 3.0.0 (synchronized across pyproject.toml, `__init__.py`, omniskill.yaml) |
| **Python requirement** | >=3.9 (tested: 3.9, 3.12, 3.13) |
| **License** | MIT |

## pyproject.toml Analysis (v3.0.0)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "omniskill"
version = "3.0.0"
requires-python = ">=3.9"

dependencies = [
    "typer>=0.9.0",
    "rich>=13.0.0",
    "PyYAML>=6.0",
    "platformdirs>=3.0.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "pytest-cov>=4.0", "ruff>=0.4.0"]

[project.scripts]
omniskill = "omniskill.cli:app"
```

> **v3.0.0 FIXED:** Runtime dependencies, dev dependencies, and CLI entry point were all missing in v2. All three gaps resolved.

## CI/CD Status (v3.0.0)

**GitHub Actions CI added** — `.github/workflows/ci.yml`
- Matrix testing: Python 3.9, 3.12, 3.13
- Steps: checkout → install (`pip install -e ".[dev]"`) → `omniskill validate` → `pytest tests/` → `ruff check` (3.12 only)
- Triggers: push and pull_request to `main`/`master`

> **v3.0.0 FIXED:** No CI/CD existed in v2. GitHub Actions workflow with matrix testing added.

## Scripts (`scripts/`, 11 files, 5,792 lines)

| Script | Purpose |
|--------|---------|
| `install.py` | Platform-aware skill installation |
| `validate.py` | Standalone manifest validation |
| `doctor.py` | Health check diagnostics |
| `admin.py` | Framework statistics dashboard |
| `migrate.py` | Legacy format migration |
| `update.py` | Update checking |
| `build_docs.py` | Documentation site builder |
| `generate-agent-cards.py` | Agent card generation |
| `generate-llms-txt.py` | llms.txt file generation |
| `batch-upgrade-stubs.py` | Batch upgrade stub skills to gold |
| `skill-compliance-check.py` | Skill compliance verification |

## Build & Install Commands

```bash
# Install from local (editable)
pip install -e .

# Install from PyPI (once published)
pip install omniskill

# Run tests
python -m pytest tests/ -v

# Build distribution
pip install build && python -m build

# Run CLI
python -m omniskill --version
```

## Version (v3.0.0 — Synchronized)

| Source | Version |
|--------|---------|
| `pyproject.toml` | 3.0.0 |
| `__init__.py` | 3.0.0 |
| `omniskill.yaml` | 3.0.0 |
| `omniskill doctor` output | 3.0.0 |
| `omniskill --version` output | 3.0.0 |

> **v3.0.0 FIXED:** All three version sources previously disagreed (0.2.0, 2.0.0, 2.0.0). All are now synchronized to 3.0.0.

## Documentation Site

- Built via `scripts/build_docs.py`
- Output: `docs/html/` (44 HTML files)
- Hosted at: https://sufficientdaikon.github.io/omniskill/docs/html/index.html
- No automated doc deployment (no GitHub Pages workflow)
