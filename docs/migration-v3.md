# Migration Guide: v2.0.0 → v3.0.0

## What Changed

OMNISKILL v3.0.0 adds **Layer 6: Runtime Contracts** — a new layer that wraps the entire runtime with enforced session lifecycle, policy-gated tool execution, versioned telemetry, replay determinism, and MCP trust routing.

**The upgrade is fully backward compatible.** All existing v2 skills, agents, bundles, pipelines, schemas, hooks, and synapses continue to work without modification. v3 is purely additive.

## Breaking Changes

**None.** All existing content is forward-compatible:

- Existing `SKILL.md` + `manifest.yaml` files work unchanged
- Existing `AGENT.md` + `agent-manifest.yaml` files work unchanged
- Pipeline YAML definitions are consumed by the engine as-is
- All 9 v2 schemas preserved alongside 6 new v3 schemas
- v2 core modules (`pipeline_engine.py`, `pipeline_state.py`, `artifact_validator.py`) untouched
- All 282 v2 tests continue to pass

## New Capabilities

| Feature | Module | Description |
|---|---|---|
| **Session Lifecycle** | `session_manager.py` | 8-state machine with strict transitions, correlation IDs, persistence |
| **Central Policy Engine** | `policy_engine.py` | Default-deny tool gating with trust tiers, schema validation, audit log |
| **Telemetry & Replay** | `telemetry.py` | Versioned envelopes (3.0.0), replay snapshots, structure-only checksums |
| **MCP Trust Routing** | `agent_mcp.py` | Capability-based routing with health policies and trust tier precedence |
| **Schema Validation** | `schema_validator.py` | Schema lint, contradiction detection, v2/v3 compatibility checking |
| **Migration Runner** | `migration.py` | Dry-run analysis, release gate scorecard, 6 hard gates |

## New Schemas (6)

| Schema | Purpose |
|---|---|
| `session.schema.yaml` | Session lifecycle states and transitions |
| `tool-invocation.schema.yaml` | Tool call with required policy decision |
| `permission.schema.yaml` | Permission rules with trust tiers |
| `hook-event.schema.yaml` | Normalized hook bus events |
| `telemetry-envelope.schema.yaml` | Versioned telemetry format |
| `context-handoff.schema.yaml` | Phase handoff with pinned constraints and evidence |

## New Directory Structure

```
src/omniskill/core/
├── pipeline_engine.py       # v2 — unchanged
├── pipeline_state.py        # v2 — unchanged
├── artifact_validator.py    # v2 — unchanged
├── schema_validator.py      # NEW v3 — schema lint + compatibility
├── session_manager.py       # NEW v3 — session lifecycle state machine
├── policy_engine.py         # NEW v3 — policy-gated tool execution
├── telemetry.py             # NEW v3 — telemetry envelopes + replay
├── agent_mcp.py             # NEW v3 — agent profiles + MCP routing
└── migration.py             # NEW v3 — migration runner + release gates

schemas/
├── (9 existing v2 schemas)  # Preserved
├── session.schema.yaml      # NEW v3
├── tool-invocation.schema.yaml  # NEW v3
├── permission.schema.yaml   # NEW v3
├── hook-event.schema.yaml   # NEW v3
├── telemetry-envelope.schema.yaml  # NEW v3
└── context-handoff.schema.yaml    # NEW v3

tests/
├── (v2 test files)          # 282 tests — all pass
├── test_v3_contracts.py     # NEW — 79 tests
├── test_v3_session.py       # NEW — 41 tests
├── test_v3_policy.py        # NEW — 26 tests
├── test_v3_telemetry.py     # NEW — 29 tests
├── test_v3_migration.py     # NEW — 23 tests
└── test_v3_agent_mcp.py     # NEW — 20 tests
```

## Session Lifecycle

The `SessionManager` enforces an 8-state lifecycle:

```
created → active → waiting_tool → active
                 → waiting_permission → active
                 → idle → active
                 → error → recovering → active
                 → archived (terminal)
```

Invalid transitions raise `InvalidTransitionError`. Every event is logged with a correlation ID.

## Policy Engine

The `PolicyEngine` gates every tool invocation:

1. **Schema validation** — tool arguments checked against registered schemas
2. **Permission rules** — evaluated in order, first match wins
3. **Trust tier precedence** — builtin > verified > community > untrusted
4. **Decision artifact** — machine-readable `PolicyDecision` with rationale

Default action is **deny**. Denied decisions are queryable from the audit log.

## Using v3 SDK

```python
from src.omniskill.core.session_manager import Session
from src.omniskill.core.policy_engine import PolicyEngine, PermissionRule
from src.omniskill.core.telemetry import TelemetryCollector, ReplayHarness

# Session lifecycle
session = Session.create("my-pipeline", {"input": "Build auth"})
session.activate()
session.wait_for_tool("file_write")
session.resume()

# Policy engine
engine = PolicyEngine()
engine.add_rule(PermissionRule(id="r1", scope="file_*", trust_tier="verified", action="allow"))
decision = engine.evaluate("file_write", {"path": "/src/main.py"}, trust_tier="verified")

# Telemetry
collector = TelemetryCollector()
collector.emit_from_session_event(session, "session_start")
collector.emit_from_policy_decision(decision)

# Replay determinism
harness = ReplayHarness(collector)
baseline = harness.capture(session)
current = harness.capture(session)
result = harness.compare(baseline, current)
assert result["deterministic"] is True
```

## Release Gates

The `ReleaseGateValidator` validates 6 hard gates:

| Gate | What It Checks |
|---|---|
| SchemaAndContracts | All v3 schemas present and version 3.x |
| PolicyAndSecurity | Policy engine and permission schema present |
| ReplayDeterminism | Telemetry module and replay tests present |
| ContextIntegrity | Handoff schema enforces pinned_constraints and evidence_links |
| PromptQuality | Prompt files present, schema validator functional |
| MigrationReadiness | Migration dry-run passes with zero blockers |

All 6 must pass, weighted score must reach 90+ for GO recommendation.

## Upgrade Steps

1. **Pull the latest version** — `git pull` or update your copy to v3.0.0
2. **No migration required** — existing v2 content works as-is
3. **Run tests** — `python -m pytest tests/` to verify all 500 tests pass
4. **Optional:** Use the new `SessionManager` for session lifecycle tracking
5. **Optional:** Use the `PolicyEngine` for policy-gated tool execution
6. **Optional:** Use the `TelemetryCollector` for structured observability

That's it. All 282 v2 tests + 218 v3 tests = 500/500 PASS.
