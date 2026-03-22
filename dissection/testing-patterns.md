# Testing Patterns

## Test Suite Overview

| Metric | Value |
|--------|-------|
| **Framework** | pytest 9.0.2 |
| **Total Tests** | 513 collected |
| **Passed** | 507 (98.8%) |
| **Failed** | 6 (1.2%) |
| **Duration** | ~6.5 seconds |
| **Test Files** | 16 files |
| **Total Lines** | 4,005 |

## Test Files

| File | Tests | Category | What It Tests |
|------|-------|----------|---------------|
| `test_agent_guardrails.py` | ~120 | Unit | Agent manifest guardrails: enforcement, rules schema, critical rules |
| `test_artifact_validator.py` | 14 | Unit | Artifact existence, sections, min content, compliance score |
| `test_cli_pipeline.py` | 10 | Unit | Pipeline CLI commands: run, list, cancel, helpers |
| `test_guardrails.py` | 17 | Unit | Anti-rationalization synapse, schemas, forbidden phrases |
| `test_hooks.py` | 16 | Unit | All 5 hook types: session_start, pre_step, post_step, on_failure, on_deviation |
| `test_integration.py` | 11 | Integration | End-to-end pipeline flow, hook integration, SDK, manifest consistency |
| `test_pipeline_engine.py` | ~30 | Unit | Pipeline loading, step execution, state machine, failure handling |
| `test_pipeline_state.py` | ~20 | Unit | State creation, persistence, loading, status updates |
| `test_sequential_thinking.py` | ~15 | Unit | Sequential thinking synapse |
| `test_v3_agent_mcp.py` | ~30 | Unit (v3) | MCP trust routing, connector management |
| `test_v3_contracts.py` | ~30 | Unit (v3) | v3 schema contracts |
| `test_v3_migration.py` | ~30 | Unit (v3) | Migration engine, release gate validator |
| `test_v3_policy.py` | ~30 | Unit (v3) | Policy engine: evaluation, rules, audit log |
| `test_v3_session.py` | ~40 | Unit (v3) | Session state machine, transitions, persistence |
| `test_v3_telemetry.py` | ~20 | Unit (v3) | Telemetry envelopes, replay |
| `stress/test_stress.py` | 13 | Stress | Large pipelines (20 steps), cascading failures, state corruption, edge cases |

## Test Patterns

### Fixture Usage
- Tests use pytest fixtures for temporary directories (`tmp_path`)
- OMNISKILL_ROOT resolved at test time for actual repo-based testing
- Agent/synapse tests parameterize over all discovered directories

### Parameterized Testing
Heavy use of `@pytest.mark.parametrize` across agent names:
```python
# test_agent_guardrails.py parameterizes over all 10 agents
test_manifest_file_exists[context-curator-agent]
test_manifest_file_exists[debugger-agent]
...
```

### Test Categories
1. **Schema validation tests** — Check YAML manifests against expected fields
2. **Behavioral tests** — Verify state machine transitions, hook firing
3. **Integration tests** — End-to-end pipeline execution with persistence
4. **Stress tests** — 20-step pipelines, corrupted JSON handling, binary files
5. **v3 contract tests** — Validate new v3 modules (session, policy, telemetry)

## Failing Tests (6)

All 6 failures are in `test_agent_guardrails.py` for `security-reviewer-agent`:
- Missing `guardrail-enforcement` key in manifest
- Non-standard guardrail rule format (strings instead of dicts with `rule` key)
- Root cause: `security-reviewer-agent` manifest uses a different guardrail format than the other 9 agents

## Coverage Gaps

| Module | Has Tests? |
|--------|-----------|
| `core/registry.py` | Indirectly via integration |
| `core/pipeline_engine.py` | Yes |
| `core/session_manager.py` | Yes (test_v3_session) |
| `core/policy_engine.py` | Yes (test_v3_policy) |
| `core/schema_validator.py` | Indirectly via test_v3_contracts |
| `core/installer.py` | No dedicated test |
| `core/config.py` | No dedicated test |
| `core/agent_cards.py` | No dedicated test |
| `core/llms_txt.py` | No dedicated test |
| `commands/*.py` | Only pipeline command tested |
| `sdk/omniskill.py` | Indirectly via test_integration |
| `utils/*.py` | No dedicated test |
