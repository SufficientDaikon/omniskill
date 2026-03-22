# OMNISKILL Architecture

## Overview

OMNISKILL v3.0.0 uses a **6-layer architecture** where each layer builds on the one below. The codebase is a Python monorepo with a Typer-based CLI, a plugin-style registry, a pipeline execution engine, and platform adapters for cross-tool deployment.

## Directory Structure (Annotated)

```
omniskill/                          # Repository root
├── omniskill.yaml                  # Root manifest — single source of truth for all components
├── pyproject.toml                  # Python packaging (hatchling build backend)
├── src/omniskill/                  # Core Python package (40 files, ~9,243 lines)
│   ├── __init__.py                 # Version: 3.0.0, app name
│   ├── __main__.py                 # `python -m omniskill` entry point
│   ├── cli.py                      # Typer app — 16 CLI commands registered
│   ├── commands/                   # CLI command implementations (16 modules)
│   │   ├── admin.py                # Administration dashboard
│   │   ├── cards.py                # Agent card viewer
│   │   ├── catalog.py              # MCP server catalog browser
│   │   ├── config.py               # Get/set configuration
│   │   ├── doctor.py               # Health diagnostics
│   │   ├── generate.py             # Artifact generation
│   │   ├── info.py                 # Component information
│   │   ├── init_cmd.py             # Platform detection & setup
│   │   ├── install.py              # Skill/bundle installation
│   │   ├── list_cmd.py             # Component listing
│   │   ├── migrate.py              # Format migration
│   │   ├── pipeline.py             # Pipeline sub-app (run, list, cancel, resume, status)
│   │   ├── search.py               # Component search
│   │   ├── uninstall.py            # Component removal
│   │   ├── update.py               # Update checker
│   │   └── validate.py             # Manifest/skill validation
│   ├── core/                       # Core engine modules (15 modules)
│   │   ├── agent_cards.py          # Agent card generation
│   │   ├── agent_mcp.py            # MCP trust routing & connector management
│   │   ├── artifact_validator.py   # Pipeline artifact validation
│   │   ├── catalog.py              # MCP server catalog with dataclasses
│   │   ├── config.py               # Configuration management
│   │   ├── installer.py            # Platform installer logic
│   │   ├── llms_txt.py             # llms.txt generation
│   │   ├── migration.py            # v2→v3 migration engine, release gate validator
│   │   ├── pipeline_engine.py      # Pipeline executor, state machine, hooks
│   │   ├── pipeline_state.py       # Pipeline state persistence (JSON)
│   │   ├── platform.py             # Platform detection dataclass
│   │   ├── policy_engine.py        # v3 permission/policy evaluation
│   │   ├── registry.py             # Component registry (skills, agents, bundles, pipelines, synapses)
│   │   ├── schema_validator.py     # YAML schema linting, v2→v3 compat checker
│   │   ├── session_manager.py      # v3 session lifecycle state machine
│   │   └── telemetry.py            # Telemetry envelope & replay harness
│   └── utils/                      # Utility modules
│       ├── output.py               # Rich console, output flags, progress bars
│       └── paths.py                # Path resolution (platformdirs)
├── sdk/                            # Python SDK (1 file, 615 lines)
│   └── omniskill.py                # OmniSkill class — programmatic API
├── skills/                         # 84 directories (83 skills + _template)
├── agents/                         # 11 directories (10 agents + _template)
├── bundles/                        # 14 bundles
├── pipelines/                      # 8 pipeline YAML definitions
├── synapses/                       # 6 directories (5 synapses registered: 3 core + 2 cross-cutting)
├── schemas/                        # 15 validation schemas (9 v2 + 6 v3)
├── adapters/                       # 5 platform adapters
├── hooks/                          # 5 lifecycle hooks + hooks.yaml config
├── prompts/                        # Prompt library (router, system, personas)
├── scripts/                        # 11 admin/CLI scripts
├── tests/                          # 16 test files, 513 tests
├── catalog/                        # MCP server catalog (mcp-servers.yaml)
└── docs/                           # Documentation site + markdown guides
```

## Layer Architecture

### Layer 1 — Skills & Knowledge
- **83 skills** in universal format (SKILL.md + manifest.yaml)
- **14 bundles** grouping skills by domain
- Prompt library (router.md, system.md, shared.md, personas/)
- Knowledge sources (pluggable GitHub repos, URLs, local dirs)

### Layer 2 — Agents & Personas
- **10 agents** with formal agent-manifest.yaml (including security-reviewer-agent added in v3)
- Agent cards (machine-readable capabilities metadata)
- Skill bindings, guardrails (must-do/must-not rules), handoff protocols

### Layer 3 — Synapses & Cognition
- **5 synapses** registered (3 core + 2 cross-cutting) — all 5 now registered in v3
- Core synapses auto-fire: metacognition, anti-rationalization, sequential-thinking
- Cross-cutting: security-awareness (OWASP injection during code tasks); pattern-recognition (auxiliary)

> **v3.0.0 FIXED:** security-awareness and pattern-recognition were on disk but unregistered in v2. Both registered in v3.

### Layer 4 — Pipelines & Orchestration
- **8 pipelines** with YAML definitions
- PipelineExecutor with state machine (pending→validating→executing→completed/failed)
- StepResult tracking, accumulated state, resumable execution

### Layer 5 — Guardrails & Hooks
- **5 lifecycle hooks**: session_start, pre_step, post_step, on_failure, on_deviation
- hooks.yaml configuration with timeouts and error policies
- Anti-rationalization enforcement via Iron Laws

### Layer 6 — Runtime Contracts (v3)
- Session state machine (8 states, enforced transitions)
- Policy engine (rule-based allow/deny/escalate with audit log)
- Schema validator (lint, contradiction detection, v2→v3 compat)
- Telemetry envelope & replay harness

## Key Architectural Patterns

| Pattern | Implementation | Location |
|---------|---------------|----------|
| Registry/Repository | `Registry` class loads omniskill.yaml, caches components | `core/registry.py` |
| Pipeline/Chain | `PipelineExecutor` with ordered step execution | `core/pipeline_engine.py` |
| State Machine | `SessionStatus` enum with `_VALID_TRANSITIONS` table | `core/session_manager.py` |
| Strategy/Adapter | Platform adapters (5 strategies for different AI tools) | `adapters/` |
| Hook/Lifecycle | 5 hooks firing at pipeline lifecycle events | `hooks/` |
| Policy Engine | Rule-based access control with audit trail | `core/policy_engine.py` |
| Dataclass Models | 30+ `@dataclass` classes across core modules | `core/*.py` |
| Facade | CLI wraps all core modules via Typer commands | `cli.py` |

## Data Flow

```
User → CLI (cli.py) → Registry → Component Discovery
                     → PipelineExecutor → Hook System → Step Execution
                                        → ArtifactValidator → Quality Gates
                                        → PipelineState → JSON Persistence
                     → PolicyEngine → Permission Evaluation → Audit Log
                     → SessionManager → State Machine → Event Log
```

## Entry Points

1. **CLI**: `omniskill` (installed via `[project.scripts]`) or `python -m omniskill` → `cli.py:app` (Typer)
2. **SDK**: `from sdk.omniskill import OmniSkill` → programmatic API
3. **Scripts**: `python scripts/install.py` → standalone admin tools
4. **Hooks**: `hooks/*.py:execute()` → lifecycle event handlers
