# Best Practices

Observed practices extracted from the OMNISKILL v2.0.0 codebase, presented as actionable rules with code citations.

## Skill Authoring

### 1. Always Include All Required Manifest Fields
Every `manifest.yaml` must include: `name`, `version`, `description`, `author`, `license`, `platforms`, `tags`, `triggers`, `priority`.

**Citation:** `skills/_template/manifest.yaml` defines the canonical structure. Validation in `src/omniskill/core/schema_validator.py:lint_schema()` checks for required fields.

### 2. Use the 6-Section SKILL.md Structure
Gold-standard skills follow: Identity → When to Use → Workflow → Rules → Output Format → Handoff.

**Citation:** `skills/complexity-router/SKILL.md` is the exemplar P0 skill with all sections fully developed.

**Anti-pattern:** Stub skills with only 1-2 sections — these are flagged by `scripts/skill-compliance-check.py`.

### 3. Use kebab-case for Skill Names
All skill directories and `name:` fields use `kebab-case` (e.g., `react-best-practices`, `godot-scene-architecture`).

**Citation:** 83/83 skills follow this convention.

### 4. Declare Platform Compatibility Explicitly
List all supported platforms in `manifest.yaml`. The 5 platforms are: `claude-code`, `copilot-cli`, `cursor`, `windsurf`, `antigravity`.

**Citation:** `adapters/` directory contains platform-specific strategies that consume this field.

### 5. Use Trigger Keywords and Patterns for Routing
Every skill should have `triggers.keywords` (exact match terms) and `triggers.patterns` (glob-like patterns) to enable automatic routing.

**Citation:** `src/omniskill/core/registry.py` uses triggers for skill discovery. The `complexity-router` skill uses classification to route to the right execution mode.

## Agent Design

### 6. Bind Skills Explicitly in Agent Manifests
Agents must declare `skill-bindings` listing exactly which skills they can invoke.

**Citation:** `agents/implementer/agent-manifest.yaml` binds specific skills. The pipeline engine validates agent-skill alignment.

### 7. Define Guardrails with Severity Levels
Every agent manifest should include `guardrails` with `must-do` and `must-not` rules, each tagged with severity: `critical`, `major`, or `minor`.

**Citation:** `schemas/guardrails.schema.yaml` defines the structure. Critical guardrails trigger immediate escalation via the deviation protocol.

### 8. Use `guardrail-enforcement: strict`
Always set enforcement to `strict` so the deviation protocol activates on any violation.

**Citation:** `hooks/on_deviation.py` implements STOP → DOCUMENT → ASK → LOG when violations occur.

## Pipeline Construction

### 9. Chain Agents Through Context Curation
Between pipeline steps, use the `context-curator` agent/skill to trim irrelevant state and pass only what the next agent needs.

**Citation:** `pipelines/sdd-pipeline.yaml` chains spec-writer → context-curator → implementer → reviewer.

### 10. Design for Failure Recovery
Every pipeline should work with the `on_failure` hook's 5-action recovery model: retry → loop → escalate → halt → skip.

**Citation:** `hooks/on_failure.py:execute()` implements the 3-Fix Escape Hatch — after 3 consecutive failures, escalate to human review.

### 11. Use the 7-State Pipeline Status Model
Pipeline states: `pending` → `in_progress` → `completed` / `failed` / `paused` / `cancelled` / `unknown`. Validate transitions before applying them.

**Citation:** `src/omniskill/core/pipeline_engine.py:validate_transition()` enforces allowed state transitions.

## Code Quality

### 12. Use Dataclasses for Data Structures
All component metadata uses `@dataclass` with typed fields rather than raw dictionaries.

**Citation:** `src/omniskill/core/registry.py` defines 6 dataclasses: `Skill`, `AgentCard`, `Agent`, `Bundle`, `Pipeline`, `Synapse`.

### 13. Use `yaml.safe_load()` — Never `yaml.load()`
All YAML parsing uses `safe_load()` to prevent arbitrary code execution.

**Citation:** Every YAML read in `registry.py`, `pipeline_engine.py`, `schema_validator.py` uses `yaml.safe_load()`.

### 14. Use `pathlib.Path` for File Operations
Prefer `Path` objects over string concatenation for file paths.

**Citation:** `src/omniskill/utils/paths.py` centralizes path resolution using `pathlib`. All core modules consume these.

### 15. Centralize Console Output
Use the shared `console` object from `src/omniskill/utils/output.py` for all Rich output instead of direct `print()`.

**Citation:** All CLI commands import from `output.py`. This ensures consistent formatting and respects `--quiet`/`--json` flags.

## Registry Usage

### 16. Always Load via Registry, Not Direct File Reads
Components should be discovered through `Registry.find_skill()`, `Registry.find_agent()`, etc. — not by hardcoding paths.

**Citation:** `src/omniskill/core/registry.py:Registry.load()` is the single point of truth. The SDK wraps this in `OmniSkill.__init__()`.

### 17. Use Lazy Manifest Loading
The registry loads only lightweight metadata on startup. Full manifests (SKILL.md content, resources) are loaded on demand via `load_skill_manifest()`.

**Citation:** `registry.py:load_skill_manifest()` reads SKILL.md and resources only when a specific skill is requested.

## Security

### 18. Default-Deny in Policy Engine
The policy engine denies any action not explicitly permitted by a rule.

**Citation:** `src/omniskill/core/policy_engine.py:evaluate()` returns `deny` when no matching rule is found.

### 19. Use Trust Tiers for Access Control
Components are classified by trust: `builtin` > `verified` > `community` > `untrusted`. Higher trust overrides lower.

**Citation:** `policy_engine.py:PermissionRule` includes `trust_tier` field. Rules with higher trust take precedence.

### 20. Validate All Manifests Before Use
Run `omniskill validate` to check all manifests against schemas before deployment.

**Citation:** `src/omniskill/core/schema_validator.py:lint_all()` validates against 15 YAML schemas in `schemas/`.

## Session Management (v3)

### 21. Use Correlation IDs for Traceability
Every session gets a unique `session_id` and `correlation_id` for end-to-end tracing.

**Citation:** `src/omniskill/core/session_manager.py:Session.create()` generates UUIDs for both.

### 22. Enforce State Machine Transitions
The session state machine has 8 states with explicit allowed transitions. Never set state directly — use transition methods.

**Citation:** `session_manager.py:ALLOWED_TRANSITIONS` dictionary enforces the state graph.

### 23. Accumulate Context, Never Discard
Session context grows monotonically — new data is appended, old data is never removed. This ensures auditability.

**Citation:** `session_manager.py:Session.send()` appends to the accumulated_context list.
