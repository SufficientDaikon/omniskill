# Changelog

All notable changes to OMNISKILL will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-03-09

### Added

- **12 New Development-Workflow Skills**: Added skills for advanced development workflows, bringing the total from 49 to 61 skills

- **Guardrails Engine**: Anti-rationalization synapse with 10 Iron Laws, forbidden phrases, rationalization tables
- **Sequential Thinking Protocol**: Chain-of-thought synapse with DECOMPOSE → REASON → VALIDATE → SYNTHESIZE phases
- **Pipeline Orchestrator Engine**: Real execution engine replacing simulated pipelines (PipelineExecutor, PipelineState, ArtifactValidator)
- **Hook System**: 5 Python lifecycle hooks (session_start, pre_step, post_step, on_failure, on_deviation)
- **Enhanced Metacognition**: Stuck-loop detection, complexity scaling, escape hatch protocol, confidence calibration
- **Deviation Protocol**: STOP → DOCUMENT → ASK → LOG workflow with schema
- **Pipeline State Persistence**: JSON-based state at `~/.copilot/.omniskill/pipeline-states/`
- **Accumulated State Pattern**: Decisions, constraints, tech_stack grow across pipeline steps
- **CLI Pipeline Commands**: `run`, `status`, `resume`, `list`, `cancel`
- **SDK Pipeline Methods**: `execute_pipeline`, `resume_pipeline`, `get_pipeline_status`, `list_active_pipelines`, `cancel_pipeline`
- **SDK Synapse Methods**: `list_synapses`, `get_core_synapses`
- **3 New Schemas**: guardrails, deviation-log, thinking-trace
- **282 Tests**: 9 test files covering engine, state, validation, guardrails, hooks, thinking, integration, stress, CLI
- **4 New Documentation Guides**: architecture, guardrails, sequential-thinking, pipeline-orchestration
- **HTML Documentation Site**: Auto-generated from Markdown with Mermaid diagram rendering via `scripts/build_docs.py`
- **Enhanced Validation**: `validate.py` now supports `--synapses`, `--hooks`, `--agents`, `--all` flags

### Changed

- Version bump 0.2.0 → 2.0.0
- Pipeline execution is now real (was simulated)
- Metacognition synapse upgraded to v2.0.0
- `omniskill.yaml` now registers 3 synapses (was 1)

### Fixed

- SDK handles both dict and string synapse formats in `omniskill.yaml`
- SDK gracefully handles malformed YAML in skill manifests
- Pipeline state persists correctly to disk during execution
- Engine reloads accumulated state from disk after step handlers modify it

## [0.2.0] - 2026-03-08

### Added

- **Context Curator agent** (`agents/context-curator-agent/`) — Universal context management agent for multi-agent pipeline handoffs with validation, budget tracking, smart chunking, and dashboard generation
- **Context Curator skill** (`skills/context-curator/`) — Procedural skill with context brief templates, pipeline state JSON schema, filtering rules, compression strategies, and dashboard generation procedures
- Context Curator added to **sdd-kit** bundle (now 6 skills)
- Pipeline state persistence across sessions via JSON state files
- HTML pipeline progress dashboards (self-contained, print-friendly)
- Context budget awareness with token estimation and progressive compression

### Changed

- **sdd-pipeline** v1.1.0 — Added context-curator steps between spec-writer → implementer and implementer → reviewer transitions
- **ux-pipeline** v1.1.0 — Added context-curator steps between research → wireframe and wireframe → visual-design transitions
- **debug-pipeline** v1.1.0 — Added context-curator step between investigate → fix transition
- **skill-factory** v1.1.0 — Added context-curator step between specify → implement transition
- **full-product** v1.1.0 — Added context-curator steps between ux-design → specify, specify → implement, and implement → review transitions
- All curator steps use `on-failure: skip` for backward compatibility (pipelines work without curator)

## [0.1.0] - 2026-03-08

### Added

- Initial repository scaffolding and directory structure
- Universal skill format: `SKILL.md` + `manifest.yaml`
- Universal agent format: `AGENT.md` + `agent-manifest.yaml`
- YAML validation schemas for skills, bundles, agents, and pipelines
- Skill template (`skills/_template/`) with full directory structure
- Agent template (`agents/_template/`) with full directory structure
- Root manifest (`omniskill.yaml`) registering all components
- 8 bundle definitions: godot-kit, web-dev-kit, ux-design-kit, django-kit, sdd-kit, testing-kit, mobile-kit, meta-kit
- 5 pipeline definitions: sdd-pipeline, ux-pipeline, debug-pipeline, skill-factory, full-product
- Cross-platform adapter stubs for: Claude Code, Copilot CLI, Cursor, Windsurf, Antigravity
- Comprehensive README with catalog and quick-start guide
- Contributing guidelines
- MIT License
