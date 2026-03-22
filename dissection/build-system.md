# Build System

## Build Configuration

| Aspect | Value |
|--------|-------|
| **Build backend** | hatchling 1.29.0 |
| **Package format** | PEP 517/518 via pyproject.toml |
| **Source layout** | `src/omniskill/` (src-layout) |
| **Version** | 2.0.0 (pyproject.toml), 0.2.0 (__init__.py) |
| **Python requirement** | >=3.9 |
| **License** | MIT |

## pyproject.toml Analysis

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"   # Fixed during dissection (was "hatchling.backends")

[project]
name = "omniskill"
version = "2.0.0"
requires-python = ">=3.9"
# NOTE: No [project.dependencies] — runtime deps undeclared
# NOTE: No [project.scripts] — no CLI entry point
# NOTE: No [project.optional-dependencies] — no dev deps
```

## CI/CD Status

**No CI/CD pipelines configured.**
- No `.github/workflows/` directory
- No `.gitlab-ci.yml`
- No Dockerfile or docker-compose.yml
- No Makefile or tox.ini
- No `.editorconfig`
- No linting configuration (no ruff.toml, .flake8, .pylintrc)

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

## Version Discrepancy

| Source | Version |
|--------|---------|
| `pyproject.toml` | 2.0.0 |
| `__init__.py` | 0.2.0 |
| `omniskill.yaml` | 2.0.0 |
| `omniskill doctor` output | 2.0.0 |
| `omniskill --version` output | 0.2.0 |

The CLI reports `0.2.0` from `__init__.py`, while the framework manifest says `2.0.0`. These should be synchronized.

## Documentation Site

- Built via `scripts/build_docs.py`
- Output: `docs/html/` (44 HTML files)
- Hosted at: https://sufficientdaikon.github.io/omniskill/docs/html/index.html
- No automated doc deployment (no GitHub Pages workflow)
