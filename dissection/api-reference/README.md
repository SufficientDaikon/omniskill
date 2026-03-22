# API Reference

## 1. CLI Commands (16 commands via Typer)

### Top-Level Commands

| Command | Help Text | Module |
|---------|-----------|--------|
| `omniskill init` | Initialize OMNISKILL — detect platforms, create config | `commands/init_cmd.py` |
| `omniskill install` | Install skills, bundles, or agents to platform(s) | `commands/install.py` |
| `omniskill uninstall` | Remove installed components from platform(s) | `commands/uninstall.py` |
| `omniskill doctor` | Health diagnostics with score and platform status | `commands/doctor.py` |
| `omniskill validate` | Validate manifests and skill files | `commands/validate.py` |
| `omniskill list [TYPE]` | List available skills, agents, bundles, or pipelines | `commands/list_cmd.py` |
| `omniskill search` | Search components by keyword, tag, or description | `commands/search.py` |
| `omniskill info` | Show detailed information about a component | `commands/info.py` |
| `omniskill update` | Check for or apply OMNISKILL updates | `commands/update.py` |
| `omniskill migrate` | Convert legacy skill formats to OMNISKILL format | `commands/migrate.py` |
| `omniskill admin` | Administration dashboard with aggregate statistics | `commands/admin.py` |
| `omniskill config` | Get or set configuration values | `commands/config.py` |
| `omniskill cards` | View and manage agent cards | `commands/cards.py` |

### Sub-Apps (Nested Command Groups)

**`omniskill pipeline`** (5 subcommands):
| Subcommand | Description |
|-----------|-------------|
| `pipeline run <name>` | Execute a pipeline |
| `pipeline list` | List pipeline executions |
| `pipeline status <id>` | Show pipeline execution status |
| `pipeline cancel <id>` | Cancel a running pipeline |
| `pipeline resume <id>` | Resume a paused/failed pipeline |

**`omniskill generate`** (artifact generation sub-app)

**`omniskill catalog`** (MCP server catalog sub-app)

### Global Options
| Flag | Description |
|------|-------------|
| `--version`, `-V` | Show version and exit |
| `--json` | Output machine-readable JSON |
| `--quiet`, `-q` | Suppress non-error output |
| `--verbose`, `-v` | Increase output detail |

## 2. Python SDK (15 public methods)

**Module:** `sdk/omniskill.py` → `class OmniSkill`

### Initialization
```python
from sdk.omniskill import OmniSkill
os = OmniSkill(root_path=None)  # Auto-detects from OMNISKILL_ROOT env, ~/.omniskill/, or cwd
```

### Component Discovery
| Method | Signature | Returns |
|--------|-----------|---------|
| `list_skills()` | `(tags=None, platform=None, bundle=None)` | `list[dict]` — name, path, version, description, tags, priority |
| `list_bundles()` | `()` | `list[dict]` — name, path, skills, description, version |
| `get_skill()` | `(name: str)` | `dict` — manifest, content, path, resources |
| `list_synapses()` | `()` | `list[dict]` — name, version, type, description, phases |
| `get_core_synapses()` | `()` | `list[str]` — names of always-on synapses |

### Operations
| Method | Signature | Returns |
|--------|-----------|---------|
| `route()` | `(query: str)` | `dict` — classification, token_count, model_tier, execution_mode |
| `install()` | `(platform=None, bundle=None, skill=None, target=None)` | `bool` |
| `validate()` | `(target=None)` | `dict` — valid, errors, warnings |
| `sync_sources()` | `(source_id=None, force=False)` | `bool` |
| `health_check()` | `()` | `dict` — status, counts, version |

### Pipeline Management
| Method | Signature | Returns |
|--------|-----------|---------|
| `execute_pipeline()` | `(name, project_dir=".", config=None)` | `dict` — pipeline state |
| `resume_pipeline()` | `(state_id: str)` | `dict` — updated state |
| `get_pipeline_status()` | `(state_id: str)` | `dict | None` |
| `list_active_pipelines()` | `()` | `list[dict]` — active pipeline summaries |
| `cancel_pipeline()` | `(state_id: str)` | `bool` |

### Convenience Function
```python
from sdk.omniskill import load_skill
skill_data = load_skill("godot-best-practices")
```

## 3. Configuration Interfaces

### omniskill.yaml (Root Manifest)
```yaml
name: omniskill
version: 2.0.0
skills: [{name, path, version, tags, priority}]
bundles: [{name, path, skills: []}]
agents: [{name, path}]
synapses: [{name, path, version, type}]
pipelines: [{name, path, trigger}]
platforms: [{id, adapter, target}]
catalog: {path, schema}
```

### Pipeline YAML
```yaml
name: sdd-pipeline
version: 1.0.0
trigger: "build feature * from scratch"
synapse-mode: standard
resumable: true
artifact-persistence: project-local
steps:
  - name: step-name
    agent: agent-name
    output: expected-artifact
    on-failure: retry|halt|skip|loop|escalate
    validation: {expected-artifacts: [{path-pattern}]}
```

### hooks.yaml
```yaml
hooks:
  session-start: {enabled, handler, timeout, on-error}
  pre-step: {enabled, handler, timeout, on-error, config}
  post-step: {enabled, handler, timeout, on-error, config}
  on-failure: {enabled, handler, timeout, on-error, config}
  on-deviation: {enabled, handler, timeout, on-error}
settings:
  strict-mode: true
  log-all-events: true
```

## 4. Schema Catalog (15 schemas)

### v2 Schemas (9)
`agent-manifest`, `bundle-manifest`, `deviation-log`, `guardrails`, `mcp-catalog`, `pipeline`, `skill-manifest`, `synapse-manifest`, `thinking-trace`

### v3 Schemas (6, additive)
`session`, `tool-invocation`, `permission`, `hook-event`, `telemetry-envelope`, `context-handoff`
