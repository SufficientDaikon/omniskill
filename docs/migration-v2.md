# Migration Guide: v0.2.0 → v2.0.0

## What Changed

OMNISKILL v2.0.0 upgrades from a **passive skill/agent framework** to an **active execution platform**. Pipelines now run through a real orchestrator engine, guardrails are enforced (not just documented), and sequential thinking is a first-class protocol.

**The upgrade is fully backward compatible.** Existing skills, agents, bundles, and pipelines continue to work without modification.

## Breaking Changes

**None.** All existing content is forward-compatible:

- Existing `SKILL.md` + `manifest.yaml` files work unchanged
- Existing `AGENT.md` + `agent-manifest.yaml` files work unchanged
- Pipeline YAML definitions are consumed by the new engine as-is
- Bundle definitions are unchanged
- Adapter configurations are unchanged

## New Capabilities

| Feature | Description |
|---|---|
| **Pipeline Orchestrator** | Real execution engine with `PipelineExecutor`, `PipelineState`, `ArtifactValidator` |
| **Guardrails Engine** | 10 Iron Laws enforced at runtime; anti-rationalization detection |
| **Sequential Thinking** | DECOMPOSE → REASON → VALIDATE → SYNTHESIZE chain-of-thought |
| **Lifecycle Hooks** | Python hooks for session_start, pre_step, post_step, on_failure, on_deviation |
| **Deviation Protocol** | STOP → DOCUMENT → ASK → LOG workflow when agents go off-spec |
| **Enhanced Metacognition** | Stuck-loop detection, complexity scaling, escape hatch, confidence calibration |
| **State Persistence** | Pipeline state saved to disk; survives session restarts |
| **CLI Commands** | `run`, `status`, `resume`, `list`, `cancel` for pipelines |

## New Directory Structure

```
omniskill/
├── hooks/                          # NEW — Python lifecycle hooks
│   ├── session_start.py
│   ├── pre_step.py
│   ├── post_step.py
│   ├── on_failure.py
│   └── on_deviation.py
├── synapses/
│   ├── metacognition.md            # Upgraded to v2.0.0
│   ├── guardrails.md               # NEW — Anti-rationalization engine
│   └── sequential-thinking.md      # NEW — Chain-of-thought protocol
├── schemas/
│   ├── guardrails.schema.yaml      # NEW
│   ├── deviation-log.schema.yaml   # NEW
│   └── thinking-trace.schema.yaml  # NEW
├── src/
│   ├── engine.py                   # NEW — PipelineExecutor core
│   ├── state.py                    # NEW — PipelineState management
│   └── validation.py               # NEW — ArtifactValidator
├── tests/                          # NEW — 150 tests across 8 files
└── docs/
    ├── architecture.md             # NEW
    ├── guardrails.md               # NEW
    ├── sequential-thinking.md      # NEW
    └── pipeline-orchestration.md   # NEW
```

## Using the New Pipeline Engine

### CLI

```bash
# Run a pipeline
python scripts/admin.py --pipeline run sdd-pipeline --input "Build auth system"

# Check status
python scripts/admin.py --pipeline status <pipeline-id>

# Resume a paused/failed pipeline
python scripts/admin.py --pipeline resume <pipeline-id>

# List active pipelines
python scripts/admin.py --pipeline list

# Cancel a running pipeline
python scripts/admin.py --pipeline cancel <pipeline-id>
```

### SDK

```python
from sdk.omniskill import OmniSkill

os = OmniSkill()
pid = os.execute_pipeline("sdd-pipeline", {"input": "Build auth system"})
status = os.get_pipeline_status(pid)
os.resume_pipeline(pid)
os.cancel_pipeline(pid)
```

## Guardrails: Before vs. After

**Before (v0.2.0):** Guardrails were prose guidance in the metacognition synapse. Agents could acknowledge them and move on.

**After (v2.0.0):** Guardrails are an **enforced engine** with:
- **10 Iron Laws** — hard constraints checked at every step
- **Forbidden phrases** — patterns that trigger automatic deviation flags
- **Rationalization tables** — known rationalization patterns mapped to correct responses
- **Anti-rationalization synapse** — active detection of agents justifying spec deviations

Violations trigger the **Deviation Protocol**: STOP → DOCUMENT → ASK → LOG. The agent must pause, document the deviation, get explicit approval, and log the outcome.

## Upgrade Steps

1. **Pull the latest version** — `git pull` or update your copy to v2.0.0
2. **No migration required** — existing skills, agents, and pipelines work as-is
3. **Optional:** Add lifecycle hooks in `hooks/` to customize pipeline behavior
4. **Optional:** Use the new CLI/SDK pipeline commands for real orchestration
5. **Run tests** — `python -m pytest tests/` to verify everything works

That's it. Your existing OMNISKILL content is fully compatible with v2.0.0.
