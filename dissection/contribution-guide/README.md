# Contribution Guide

## Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/SufficientDaikon/omniskill.git
cd omniskill

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# 3. Install dependencies (not declared in pyproject.toml, install manually)
pip install typer rich pyyaml platformdirs pytest hatchling

# 4. Install omniskill in editable mode
pip install -e .

# 5. Verify installation
python -m omniskill --version
python -m omniskill doctor

# 6. Run tests
python -m pytest tests/ -v
```

## Adding a New Skill

1. Copy the template:
   ```bash
   cp -r skills/_template skills/my-new-skill
   ```

2. Edit `skills/my-new-skill/manifest.yaml`:
   - Set `name`, `version`, `description`, `author`, `license`
   - Add `platforms`, `tags`, `triggers.keywords`, `triggers.patterns`
   - Set `priority` (P0=critical, P1=high, P2=normal, P3=low, P4=optional)

3. Write `skills/my-new-skill/SKILL.md` with sections:
   - `## Identity` — Agent persona
   - `## When to Use` — Trigger conditions (start with "Use when...")
   - `## Workflow` — Step-by-step process
   - `## Rules` — DO/DON'T lists
   - `## Output Format` — Expected output structure
   - `## Handoff` — Next agent/skill in chain

4. Register in `omniskill.yaml` under `skills:`:
   ```yaml
   - name: my-new-skill
     path: skills/my-new-skill
     version: 1.0.0
     tags: [relevant, tags]
   ```

5. Validate:
   ```bash
   python -m omniskill validate
   ```

## Adding a New Agent

1. Copy template: `cp -r agents/_template agents/my-agent`
2. Write `AGENT.md` with full instructions
3. Write `agent-manifest.yaml` with required fields:
   - `name`, `version`, `role`, `description`
   - `persona`, `skill-bindings`, `input-contract`, `output-contract`
   - `guardrails` (must-do/must-not rules with severity)
   - `guardrail-enforcement: strict`
4. Register in `omniskill.yaml` under `agents:`

## Adding a New Bundle

1. Create `bundles/my-bundle/bundle.yaml`
2. List member skills
3. Create optional `bundles/my-bundle/META-SKILL.md` for routing
4. Register in `omniskill.yaml` under `bundles:`

## Coding Standards

- **Python:** snake_case variables/functions, PascalCase classes, type hints on all public functions
- **Imports:** `from __future__ import annotations` first, then stdlib → third-party → internal
- **YAML:** kebab-case keys, 2-space indentation
- **Skill names:** kebab-case, descriptive (e.g., `react-best-practices`)
- **Docstrings:** Google-style with Args/Returns sections
- **Error handling:** Specific exceptions preferred; catch-all only at system boundaries

## Running Tests

```bash
# Full suite
python -m pytest tests/ -v

# Specific test file
python -m pytest tests/test_pipeline_engine.py -v

# With output
python -m pytest tests/ -v --tb=short

# Stress tests only
python -m pytest tests/stress/ -v
```

## Validation

```bash
# Validate everything
PYTHONIOENCODING=utf-8 python -m omniskill validate

# Health check
PYTHONIOENCODING=utf-8 python -m omniskill doctor
```

Note: On Windows, set `PYTHONIOENCODING=utf-8` to avoid Unicode emoji encoding errors with Rich output.
