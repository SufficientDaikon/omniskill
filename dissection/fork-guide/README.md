# Fork Guide

## Module Classification

### Core (Must Keep)
These modules define OMNISKILL's identity and cannot be removed without breaking the framework:

| Module | Why Core |
|--------|----------|
| `src/omniskill/core/registry.py` | Central component discovery — everything depends on it |
| `src/omniskill/cli.py` | CLI entry point |
| `src/omniskill/__init__.py` | Package identity & version |
| `src/omniskill/utils/paths.py` | Path resolution used everywhere |
| `src/omniskill/utils/output.py` | Console output shared across all commands |
| `omniskill.yaml` | Root manifest — registry data source |

### Extension (Can Replace/Extend)
These implement specific features and can be swapped:

| Module | Extension Point |
|--------|----------------|
| `src/omniskill/core/pipeline_engine.py` | Replace with custom execution engine |
| `src/omniskill/core/policy_engine.py` | Replace with custom auth/policy |
| `src/omniskill/core/session_manager.py` | Replace with custom session handling |
| `src/omniskill/core/schema_validator.py` | Replace with custom validation |
| `hooks/*.py` | Replace/add lifecycle hooks |
| `adapters/` | Add new platform adapters |

### Application (Can Remove Entirely)
These are domain-specific and not required for the core framework:

| Module | What It Provides |
|--------|-----------------|
| `skills/godot-*` (5 skills) | Godot game engine skills |
| `skills/django-*` (4 skills) | Django web framework skills |
| `skills/ux-*` (5 skills) | UX design skills |
| `bundles/` (all 12) | Pre-built domain kits |
| `agents/` (all 9) | Pre-built agent personas |
| `pipelines/` (all 8) | Pre-built workflows |
| `synapses/` (all 5) | Cognitive capabilities |
| `docs/` | Documentation site |
| `scripts/` | Admin scripts |

### Configuration (Must Customize)
| File | What to Change |
|------|---------------|
| `omniskill.yaml` | Remove skills/agents you don't need, add your own |
| `pyproject.toml` | Change name, version, author, description |
| `src/omniskill/__init__.py` | Update version |
| `adapters/` | Keep only platforms you target |

## Fork Workflow

### 1. Minimal Fork (Skills-Only)
Keep only: `omniskill.yaml`, `skills/`, `adapters/`, `src/`, `sdk/`
Remove: `agents/`, `pipelines/`, `synapses/`, `hooks/`, `bundles/`, `docs/`, `scripts/`

### 2. Framework Fork (Custom Agents + Skills)
Keep everything, customize:
- Remove skills you don't need from `skills/` and `omniskill.yaml`
- Add your own skills, agents, pipelines
- Customize hooks for your workflow

### 3. White-Label Fork
Use the `rename-project` skill:
```bash
# Follow the rename-project skill to fully rebrand
# Changes: package name, CLI name, all references
```

## Extension Points

| Extension | How to Extend |
|-----------|---------------|
| New platform | Create `adapters/my-platform/`, add to `omniskill.yaml` |
| New hook | Create `hooks/my_hook.py` with `execute(context)`, add to `hooks.yaml` |
| New CLI command | Create `src/omniskill/commands/my_cmd.py`, register in `cli.py` |
| New schema | Create `schemas/my.schema.yaml`, reference in validation |
| New synapse | Create `synapses/my-synapse/` with SYNAPSE.md + manifest.yaml |

## Divergence Strategy

When forking, plan for upstream sync:
1. **Don't modify core files** — extend via hooks and adapters instead
2. **Keep omniskill.yaml structure** — add entries, don't restructure
3. **Add skills in separate directories** — don't modify existing skills
4. **Version your fork** — use different version numbers from upstream
