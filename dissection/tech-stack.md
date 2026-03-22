# Tech Stack

## Language & Runtime

| Component | Technology | Version |
|-----------|-----------|---------|
| **Primary Language** | Python | >=3.9 (tested on 3.13) |
| **Build System** | Hatchling | 1.29.0 |
| **Package Format** | PEP 517/518 (pyproject.toml) | — |
| **CLI Framework** | Typer | 0.24.1 |
| **Console Output** | Rich | 14.3.3 |
| **YAML Parsing** | PyYAML | 6.0.3 |
| **Path Resolution** | platformdirs | 4.9.4 |
| **Testing** | pytest | 9.0.2 |

## Architecture Breakdown

| Category | Count | File Types |
|----------|-------|-----------|
| Python source (src/) | 40 files | .py |
| Python tests | 16 files | .py |
| Python scripts | 11 files | .py |
| Python SDK | 1 file | .py |
| YAML configs/schemas | ~254 files | .yaml, .yml |
| Markdown docs/skills | ~335 files | .md |
| HTML docs | 44 files | .html |
| JSON configs | 15 files | .json |

## Line Counts

| Component | Lines of Code |
|-----------|--------------|
| src/omniskill/ | 9,243 |
| tests/ | 4,005 |
| scripts/ | 5,792 |
| sdk/ | 615 |
| **Total Python** | **~19,655** |

## Dependencies

### Runtime Dependencies (undeclared in pyproject.toml)
| Package | Usage |
|---------|-------|
| `typer` | CLI framework (all commands) |
| `rich` | Console output, tables, progress |
| `pyyaml` | YAML parsing (manifests, schemas, pipelines) |
| `platformdirs` | Cross-platform path resolution |

### Dev Dependencies
| Package | Usage |
|---------|-------|
| `pytest` | Test runner |
| `hatchling` | Build backend |

## CI/CD

- **No CI/CD pipelines configured** (no `.github/workflows/`, no Dockerfile, no `.gitlab-ci.yml`)
- No `.editorconfig` or linting configuration
- Testing is manual: `python -m pytest tests/`

## Platform Targets

| Platform | Adapter | Install Path |
|----------|---------|-------------|
| Claude Code | `adapters/claude-code/` | `~/.claude/skills/` |
| GitHub Copilot CLI | `adapters/copilot-cli/` | `~/.copilot/skills/` |
| Cursor | `adapters/cursor/` | `.cursor/rules/` |
| Windsurf | `adapters/windsurf/` | `.windsurfrules` |
| Antigravity | `adapters/antigravity/` | `.antigravity/skills/` |
