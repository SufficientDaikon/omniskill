# Design Patterns

## Identified Patterns

### 1. Registry Pattern (Confidence: HIGH)
**Location:** `src/omniskill/core/registry.py:95`

The `Registry` class is the central component repository. It parses `omniskill.yaml` and provides lookup methods for skills, agents, bundles, pipelines, and synapses.

```python
class Registry:
    def __init__(self, root: Path | None = None):
        self.skills: list[Skill] = []
        self.agents: list[Agent] = []
        self.bundles: list[Bundle] = []
        self.pipelines: list[Pipeline] = []
        self.synapses: list[Synapse] = []

    def load(self) -> None:       # Parse omniskill.yaml
    def find_skill(self, name)    # Lookup by name
    def find_component(self, name) # Cross-type lookup
    def similar_names(self, query) # Fuzzy matching
```

**Pattern characteristics:** Lazy loading (via `ensure_loaded()`), caching (loaded flag), manifest backfill on demand.

### 2. Pipeline Pattern (Confidence: HIGH)
**Location:** `src/omniskill/core/pipeline_engine.py:106`

`PipelineExecutor` orchestrates sequential step execution with state machine transitions.

```python
class PipelineExecutor:
    def execute(self, pipeline, project_dir, config, step_handler) -> dict
    def resume(self, state_id, step_handler) -> dict
    def validate_transition(self, from_step, to_step, state) -> dict
```

**Flow:** Load YAML → Fire session_start hook → For each step: pre_step hook → execute → post_step hook → handle failure → Save state → Mark complete

### 3. State Machine Pattern (Confidence: HIGH)
**Location:** `src/omniskill/core/session_manager.py:38`

Two separate state machines:
- **PipelineStatus** (7 states): pending, validating, executing, paused, completed, failed, cancelled
- **SessionStatus** (8 states): created, active, waiting_tool, waiting_permission, idle, recovering, archived, error

Both enforce valid transitions via lookup tables. Invalid transitions raise `InvalidTransitionError`.

```python
_VALID_TRANSITIONS: dict[SessionStatus, set[SessionStatus]] = {
    SessionStatus.CREATED: {SessionStatus.ACTIVE},
    SessionStatus.ACTIVE: {WAITING_TOOL, WAITING_PERMISSION, IDLE, RECOVERING, ERROR, ARCHIVED},
    SessionStatus.ERROR: {RECOVERING, ARCHIVED},
    SessionStatus.ARCHIVED: set(),  # Terminal state
}
```

### 4. Hook/Lifecycle Pattern (Confidence: HIGH)
**Location:** `hooks/*.py`, `src/omniskill/core/pipeline_engine.py:130`

5 lifecycle hooks loaded dynamically via `importlib.util.spec_from_file_location()`:
- `session_start` — Injects discipline rules (anti-rationalization, sequential thinking)
- `pre_step` — Validates prerequisites before step execution
- `post_step` — Validates outputs after step completion
- `on_failure` — Determines recovery strategy (retry/loop/escalate/halt/skip)
- `on_deviation` — STOP → DOCUMENT → ASK → LOG protocol

Each hook has: `execute(context: dict) -> dict` interface, configurable timeout and error policy.

### 5. Strategy/Adapter Pattern (Confidence: HIGH)
**Location:** `adapters/` (5 directories)

Each platform adapter provides a strategy for transforming and installing skills to different AI tools:
- `claude-code/` → `~/.claude/skills/`
- `copilot-cli/` → `~/.copilot/skills/`
- `cursor/` → `.cursor/rules/`
- `windsurf/` → `.windsurfrules`
- `antigravity/` → `.antigravity/skills/`

### 6. Policy Engine Pattern (Confidence: HIGH)
**Location:** `src/omniskill/core/policy_engine.py:70`

Rule-based access control with:
- Permission rules with scope, trust tier, conditions
- Schema validation before invocation
- Immutable `PolicyDecision` artifacts with audit trail
- Default-deny policy
- Replayable audit log

### 7. Dataclass Pattern (Confidence: HIGH, ~30 instances)
**Locations:** All `core/*.py` files

Extensive use of `@dataclass` for structured data:
- `Skill`, `Agent`, `Bundle`, `Pipeline`, `Synapse` (registry.py)
- `StepResult`, `PipelineDefinition` (pipeline_engine.py)
- `PolicyDecision`, `PermissionRule` (policy_engine.py)
- `SchemaLintResult` (schema_validator.py)
- `MCPServerEntry`, `MCPTrustProfile`, `MCPConnectorManager` (agent_mcp.py)
- `Session` (session_manager.py — not a dataclass, but uses same field patterns)

### 8. Facade Pattern (Confidence: MEDIUM)
**Location:** `src/omniskill/cli.py`

The CLI acts as a facade, wrapping all core modules into a unified command interface. Each subcommand delegates to the appropriate core module.

### 9. Template Pattern (Confidence: HIGH)
**Location:** `skills/_template/`, `agents/_template/`

Template directories establish the canonical file structure for new components. The `_template` skill contains SKILL.md + manifest.yaml + resources/ + overrides/ + tests/ + examples/ structure.

## Python Idioms

| Idiom | Frequency | Example |
|-------|-----------|---------|
| `@dataclass` with `field(default_factory=...)` | 30+ | All core data models |
| Type unions `X | None` (Python 3.10+) | Throughout | `dict | None = field(default=None)` |
| `Enum` for state values | 4 enums | PipelineStatus, StepStatus, SessionStatus |
| `from __future__ import annotations` | Every file | PEP 604 syntax in 3.9 compat |
| `yaml.safe_load()` | Every YAML read | Secure YAML parsing |
| `Path` from pathlib | Throughout | No string path manipulation |
| `__main__.py` entry point | 1 | `python -m omniskill` |
