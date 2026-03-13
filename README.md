<div align="center">

> **🚧 Work in Progress — Open Source & Community Driven**
>
> OMNISKILL is built by and for the open-source community. This project is actively evolving — contributions, ideas, and feedback are all welcome. **Fork it, remix it, break it, build on it — it's yours.** If you find it useful, give it a star and share it. If you want to make it better, open a PR. No gatekeeping, no strings attached. MIT licensed, forever free.

---

# 🧠 OMNISKILL

### Universal AI Agent & Skills Framework

**One repo. One format. Every platform. Best-in-class.**

[![Version](https://img.shields.io/badge/version-3.0.0-brightgreen)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/skills-61-blue)]()
[![Bundles](https://img.shields.io/badge/bundles-8-green)]()
[![Agents](https://img.shields.io/badge/agents-9-orange)]()
[![Pipelines](https://img.shields.io/badge/pipelines-6-red)]()
[![Synapses](https://img.shields.io/badge/synapses-3-blueviolet)]()
[![Hooks](https://img.shields.io/badge/hooks-5-yellow)]()
[![Schemas](https://img.shields.io/badge/schemas-15-lightgrey)]()
[![Platforms](https://img.shields.io/badge/platforms-5-purple)]()
[![Tests](https://img.shields.io/badge/tests-500-success)]()

_Write skills once. Run them on Claude Code, Copilot CLI, Cursor, Windsurf, and Antigravity._

</div>

---

## 🆕 What's New in v3.0

OMNISKILL v3.0 extends the v2 enforced intelligence framework with a new **Layer 6 — Runtime Contracts & Policy Engine**, adding session lifecycle management, policy-routed tool execution, telemetry, and replay determinism — all while preserving 100% v2 backward compatibility.

| Layer | What It Does |
| --- | --- |
| **Layer 1 — Skills & Knowledge** | 61 skills, 8 bundles, prompt library, knowledge sources |
| **Layer 2 — Agents & Personas** | 9 agents with formal personas, handoff contracts, and quality gates |
| **Layer 3 — Synapses & Cognition** | 3 cognitive synapses (metacognition, anti-rationalization, sequential thinking) that shape HOW agents reason |
| **Layer 4 — Pipelines & Orchestration** | 6 pipelines with real execution, context curation between steps, failure recovery |
| **Layer 5 — Guardrails & Hooks** | 5 lifecycle hooks enforcing discipline — not just documented rules, but runtime enforcement |
| **Layer 6 — Runtime Contracts** | Session state machine, central policy engine, telemetry envelopes, replay harness, MCP trust routing |

### v3.0 Key Highlights

- **📜 v3 Schema Contracts** — 6 new schemas (session, tool-invocation, permission, hook-event, telemetry-envelope, context-handoff) with enforced state machines, ID patterns, and negative fixture validation.
- **🔄 Session Lifecycle** — Full state machine (created → active → waiting → idle → recovering → archived) with enforced transitions, recovery policies, and correlation IDs linking sessions to pipeline traces.
- **🛡️ Central Policy Engine** — Every tool invocation must pass through the policy engine. Schema validation before execution. Trust-tier precedence (builtin > verified > community > untrusted). Machine-readable, replayable decision artifacts.
- **📡 Telemetry & Replay** — Versioned telemetry envelopes normalize all runtime events. Replay-first E2E harness with deterministic snapshot checksums. Stress-tested with 10k+ envelope loads.
- **🔌 MCP Trust Routing** — Connector manager with health policies (healthy/degraded/unhealthy) and deterministic capability-based routing preferring highest-trust healthy connectors.
- **🧪 500 Tests** — 282 v2 tests (zero regressions) + 218 v3 tests covering contracts, sessions, policy, telemetry, replay, stress, and migration.
- **✅ 6/6 Hard Release Gates** — SchemaAndContracts, PolicyAndSecurity, ReplayDeterminism, ContextIntegrity, PromptQuality, MigrationReadiness — all PASS with weighted score 100/100.

### v2.0 Highlights (preserved)

- **🛡️ Guardrails Engine** — Every agent has `guardrail-enforcement: strict` with must-not / must-do rules, severity levels (critical/major/minor), and on-violation actions (halt/warn/log). Guardrails are _enforced_, not just documented.
- **🧠 Sequential Thinking Protocol** — Agents decompose complex tasks step-by-step via the sequential-thinking synapse. No more jumping to conclusions.
- **🔄 Pipeline Orchestrator Engine** — Real multi-agent pipeline execution with `on-failure` strategies (halt/skip/loop), context curation between steps, and resumable state.
- **🏗️ 6-Layer Architecture** — Clean separation from knowledge (L1) through runtime contracts (L6), with each layer building on the one below.

---

## 🏁 Getting Started with v2.0

### Run a Pipeline

```bash
omniskill pipeline run sdd-pipeline --project ./myapp
```

This triggers the full Spec-Driven Development flow: **spec-writer → context-curator → implementer → context-curator → reviewer** — with automatic failure recovery and context curation between each step.

### Guardrails Auto-Enforce

Every agent loaded in v2.0 automatically enforces its guardrails. For example, the spec-writer-agent will **halt** if it detects assumed requirements (severity: critical), and **warn** if ambiguous language slips through (severity: major). No configuration needed — guardrails are built into every agent manifest.

### Sequential Thinking Auto-Activates

The sequential-thinking synapse is a **core synapse** — it fires automatically for every agent. Complex tasks are decomposed into numbered steps, each validated before proceeding. This prevents the "jump to solution" anti-pattern that plagues AI assistants.

```bash
# Other useful v2.0 commands
omniskill validate --all          # Validate everything (skills, bundles, agents, pipelines, synapses, hooks)
omniskill validate --agents       # Validate agent guardrails specifically
omniskill validate --hooks        # Validate hook system
omniskill cards                   # View machine-readable agent cards
omniskill doctor                  # Full health check
```

---

## 🚀 Get OMNISKILL

### CLI (Recommended)
```bash
pip install omniskill        # Install from PyPI
omniskill init               # Auto-detect your AI platforms
omniskill install --all      # Install all 61 skills
omniskill doctor             # Verify everything works
```

> 📖 Full command reference: [CLI Guide](docs/cli-guide.md)

### VS Code Extension
Works in **VS Code**, **Cursor**, and **Windsurf**.

Install from the VS Code Marketplace → search "OMNISKILL"

Features: Skill Explorer sidebar, Pipeline Dashboard, Health Report, 17 commands via Command Palette.

> 📖 Extension docs: [vscode-extension/README.md](vscode-extension/README.md)

### Web App
Browse skills, agents, and pipelines at [omniskill.dev](https://omniskill.dev) *(coming soon)*

Or run locally:
```bash
cd webapp && npm install && npm run dev
```

> 📖 Web app docs: [webapp/README.md](webapp/README.md)

---

## What is OMNISKILL?

OMNISKILL is a **universal framework** for AI coding assistant skills, agents, and workflows. It solves the fragmentation problem: instead of maintaining separate skill files for every AI tool, you write once in a universal format and deploy everywhere.

### Key Features

| Feature                 | Description                                                             |
| ----------------------- | ----------------------------------------------------------------------- |
| 🎯 **Universal Skills** | Single format works on 5+ AI platforms                                  |
| 📦 **Bundles**          | Install domain kits (Godot, Web Dev, UX, Django...) as one unit         |
| 🤖 **Formal Agents**    | Agents with personas, skill bindings, guardrails, and handoff protocols |
| 🔄 **Pipelines**        | Multi-agent workflows (spec → implement → review)                       |
| 🧠 **Complexity Router** | Smart routing — classifies tasks by complexity, routes to optimal model/agent |
| 📚 **Knowledge Sources** | Pluggable knowledge base — GitHub repos, local dirs, URLs. File-based search, no vector DB |
| 🔧 **Self-Customization** | AI-assisted skills that guide agents to create new skills, bundles, agents, and adapters |
| 🎭 **Prompt Library**   | Organized prompt templates — router, system, personas (expert, quick, teacher) |
| 🐍 **Python SDK**       | Programmatic access — `from sdk.omniskill import OmniSkill` |
| 🏭 **Skill Factory**    | AI-powered pipeline to create new skills that meet quality standards    |
| 🔌 **Cross-Platform**   | Adapters for Claude Code, Copilot CLI, Cursor, Windsurf, Antigravity    |
| 📖 **Rich Resources**   | Cheat sheets, style guides, decision trees bundled with skills          |
| 🧪 **Validation**       | Schema-based validation for every skill, bundle, agent, and pipeline    |
| 🧠 **Cognitive Synapses** | Enhance HOW agents think — metacognition, confidence calibration, structured reflection |
| 🔄 **Self-Improving**   | Uses its own pipelines to improve its own skills                        |
| 🩺 **Admin Dashboard**  | Comprehensive health checks, stats, and diagnostics via CLI             |
| 📄 **llms.txt**         | Machine-readable framework index for AI assistants — [llms.txt convention](https://llmstxt.org/) |
| 🃏 **Agent Cards**      | Machine-readable agent metadata — capabilities, cost tiers, quality metrics, and skills via `omniskill cards` |
| 🔌 **MCP Catalog**     | Curated catalog of 20 MCP servers — browse, search, auto-generate platform configs via `omniskill catalog` |

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/SufficientDaikon/omniskill.git
cd omniskill
```

### 2. Install for your platform

```bash
python scripts/install.py              # Auto-detects platforms
python scripts/install.py --platform claude-code   # Specific platform
python scripts/install.py --bundle web-dev-kit     # Specific bundle only
```

### 3. Verify

```bash
python scripts/doctor.py               # Check installation health
```

---

## 📦 Bundles

| Bundle            | Skills   | Description                                            |
| ----------------- | -------- | ------------------------------------------------------ |
| **godot-kit**     | 5 skills | Complete Godot 4 / GDScript development                |
| **web-dev-kit**   | 5 skills | Frontend, React, backend, design guidelines            |
| **ux-design-kit** | 7 skills | Full UX pipeline: research → wireframe → visual → test |
| **django-kit**    | 4 skills | Django framework, ORM, REST APIs                       |
| **sdd-kit**       | 6 skills | Spec-Driven Development: spec → implement → review + context curation |
| **testing-kit**   | 4 skills | E2E testing, QA planning, debugging                    |
| **mobile-kit**    | 2 skills | Mobile design, Capacitor best practices                |
| **meta-kit**      | 5 skills | Skill creation, discovery, packaging, prompts          |

---

## 🔄 Pipelines

| Pipeline           | Flow                                             | Trigger                        |
| ------------------ | ------------------------------------------------ | ------------------------------ |
| **sdd-pipeline**   | spec-writer → **context-curator** → implementer → **context-curator** → reviewer | "build feature X from scratch" |
| **ux-pipeline**    | research → **context-curator** → wireframe → **context-curator** → visual → review → handoff | "design feature X"             |
| **debug-pipeline** | debug → **context-curator** → implement → test → review                | "fix bug X"                    |
| **skill-factory**  | prompt → spec → **context-curator** → implement → validate → review    | "create a new skill for X"     |
| **full-product**   | ux-pipeline → **context-curator** → sdd-pipeline → testing             | "build product X end-to-end"   |

---

## 🧠 Synapses

Synapses are **cognitive capabilities** that enhance HOW agents think, not WHAT they do. Unlike skills (domain methodologies), synapses shape the agent's reasoning process itself.

| Synapse                     | Type | Firing Phases                          | Description                                                                          |
| --------------------------- | ---- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| **metacognition**           | core | PLAN → MONITOR → REFLECT              | Structured self-awareness: plan before acting, tag confidence, reflect on quality     |
| **anti-rationalization**    | core | DETECT → CHALLENGE → ENFORCE          | Prevents excuse-making and shortcut rationalization via 10 Iron Laws                 |
| **sequential-thinking**     | core | DECOMPOSE → REASON → VALIDATE → SYNTHESIZE | Step-by-step task decomposition — prevents jumping to conclusions                    |

**Core synapses** fire automatically for every agent. **Optional synapses** require explicit binding.

> 📖 Creating custom synapses: [docs/creating-synapses.md](docs/creating-synapses.md)

---

## 📁 Directory Structure

```
omniskill/
├── skills/           # 49 individual skills (SKILL.md + manifest.yaml)
│   ├── _template/    # Skill template for new skills
│   ├── complexity-router/  # 🧠 Smart task routing (P0 priority)
│   ├── context-curator/    # 🔗 Pipeline context management
│   ├── knowledge-sources/  # 📚 External knowledge management
│   ├── add-skill/    # 🔧 AI-assisted skill creation
│   ├── add-bundle/   # 🔧 AI-assisted bundle creation
│   ├── add-agent/    # 🔧 AI-assisted agent creation
│   ├── add-adapter/  # 🔧 AI-assisted adapter creation
│   ├── rename-project/ # 🔧 Fork & rename OMNISKILL
│   └── ...           # 40 domain skills
├── bundles/          # 8 domain bundles (bundle.yaml + meta-skill)
├── agents/           # 9 agent definitions (AGENT.md + agent-manifest.yaml + guardrails)
├── pipelines/        # 6 multi-agent workflow definitions with failure recovery
├── synapses/         # 3 cognitive synapses (SYNAPSE.md + manifest.yaml)
│   ├── _template/           # Synapse template for new synapses
│   ├── metacognition/       # Core — structured self-awareness
│   ├── anti-rationalization/ # Core — prevents excuse-making (10 Iron Laws)
│   └── sequential-thinking/ # Core — step-by-step decomposition (DECOMPOSE→REASON→VALIDATE→SYNTHESIZE)
├── hooks/            # 5 lifecycle hooks (hooks.yaml + handler .py files)
│   ├── hooks.yaml           # Hook configuration & lifecycle event mapping
│   ├── session_start.py     # Injects discipline rules at session start
│   ├── pre_step.py          # Validates prerequisites before pipeline steps
│   ├── post_step.py         # Validates outputs after pipeline steps
│   ├── on_failure.py        # Handles failures — retry, loop, escalate
│   └── on_deviation.py      # STOP → DOCUMENT → ASK → LOG protocol
├── src/              # 🔧 Core engine (v3.0)
│   └── omniskill/core/
│       ├── pipeline_engine.py    # PipelineExecutor state machine (v2)
│       ├── pipeline_state.py     # Accumulated state persistence (v2)
│       ├── artifact_validator.py # 5 artifact validation methods (v2)
│       ├── session_manager.py    # v3 Session lifecycle & state machine
│       ├── policy_engine.py      # v3 Central policy routing & audit
│       ├── schema_validator.py   # v3 Schema lint & contradiction checker
│       ├── telemetry.py          # v3 Telemetry envelopes & replay harness
│       ├── migration.py          # v3 Migration runner & release gates
│       └── agent_mcp.py          # v3 Agent profiles & MCP trust routing
├── prompts/          # 🎭 Prompt library — router, system, personas
│   ├── router.md     # Complexity classification prompts
│   ├── system.md     # Master system prompt
│   ├── shared.md     # Shared utilities & formatting
│   └── personas/     # Expert, Quick, Teacher personas
├── sdk/              # 🐍 Python SDK
│   └── omniskill.py  # Programmatic framework access
├── adapters/         # Cross-platform adapters (5 platforms)
├── schemas/          # 15 YAML validation schemas (9 v2 + 6 v3)
├── scripts/          # install, doctor, validate, migrate, update, admin, build_docs
├── tests/            # 500 automated tests (pytest — 282 v2 + 218 v3)
└── docs/             # 20 Markdown guides + HTML documentation site
    └── html/         # Generated HTML docs with Mermaid diagrams
```

---

## 🎯 Skill Format

Every skill follows the OMNISKILL universal format:

```
skills/my-skill/
├── SKILL.md           # Instructions (Identity, Workflow, Rules, Output, Handoff)
├── manifest.yaml      # Metadata (name, version, triggers, platforms, tags)
├── resources/         # Reference materials (cheat sheets, style guides)
├── examples/          # Sample interactions
├── templates/         # Output templates
├── tests/             # Validation test cases
└── overrides/         # Platform-specific overrides
```

**manifest.yaml** declares triggers, supported platforms, dependencies, and resources.
**SKILL.md** contains the actual instructions the AI agent follows.

See [`skills/_template/`](skills/_template/) for the full template.

---

## 🤖 Agent Format

Every agent follows the OMNISKILL agent format:

```
agents/my-agent/
├── AGENT.md               # Full agent definition (Identity, Persona, Workflow, Guardrails)
└── agent-manifest.yaml    # Metadata (skill bindings, handoffs, I/O contracts)
```

See [`agents/_template/`](agents/_template/) for the full template.

### Agent Cards

Every agent carries a machine-readable **Agent Card** describing its capabilities, input/output modes, cost tier, and quality metrics. Run `omniskill cards` to view them, or consume the auto-generated `agent-cards.json` programmatically.

```bash
omniskill cards                      # Rich table of all agents
omniskill cards spec-writer-agent    # Detailed card for one agent
omniskill cards --json               # JSON export
omniskill generate agent-cards       # Generate agent-cards.json
```

> 📖 Full docs: [docs/agent-cards.md](docs/agent-cards.md)

---

## 🔌 Supported Platforms

| Platform           | Adapter                 | Target Location        |
| ------------------ | ----------------------- | ---------------------- |
| Claude Code        | `adapters/claude-code/` | `~/.claude/skills/`    |
| GitHub Copilot CLI | `adapters/copilot-cli/` | `~/.copilot/skills/`   |
| Cursor             | `adapters/cursor/`      | `.cursor/rules/`       |
| Windsurf           | `adapters/windsurf/`    | `.windsurfrules`       |
| Antigravity        | `adapters/antigravity/` | `.antigravity/skills/` |

---

## 🧪 Validation & Admin

```bash
python scripts/validate.py --all                   # Validate everything (skills, bundles, pipelines, agents, synapses, hooks)
python scripts/validate.py skills/my-skill         # Validate one skill
python scripts/validate.py bundles/my-kit          # Validate one bundle
python scripts/validate.py --pipelines             # Validate all pipelines
python scripts/validate.py --agents                # Validate agent guardrails
python scripts/validate.py --synapses              # Validate all synapses
python scripts/validate.py --hooks                 # Validate hook system
python scripts/admin.py --stats                    # Show framework statistics
python scripts/admin.py --report                   # Generate full health report
```

---

## 🧠 Complexity Router

Every incoming task is automatically classified by complexity and routed to the optimal model/agent:

| Complexity | Model Tier | Routing |
| --- | --- | --- |
| **Trivial** | Fast (Haiku) | Direct answer, no skill needed |
| **Simple** | Fast + Skill | Single skill activation |
| **Moderate** | Standard + Resources | Skill with reference materials |
| **Complex** | Premium + Agent | Multi-skill agent orchestration |
| **Expert** | Premium + Pipeline | Full multi-agent pipeline |

Cost optimization happens automatically — no manual rules to maintain.

---

## 📚 Knowledge Sources

Plug any source into your knowledge base — no vector DB, no embeddings needed. File-based search with `grep`/`find`/`cat`.

```yaml
# sources config example
sources:
  - id: my-docs
    type: github
    repo: owner/repo
    branch: main
    content-path: docs
  - id: local-notes
    type: local
    path: ~/notes
  - id: reference
    type: url
    url: https://docs.example.com
```

---

## 🔧 AI-Assisted Self-Customization

OMNISKILL includes skills that guide AI agents through customizing the framework itself:

| Skill | Purpose |
| --- | --- |
| `add-skill` | Step-by-step guide to create a new skill |
| `add-bundle` | Create a new domain bundle with meta-skill |
| `add-agent` | Define a new agent with skill bindings |
| `add-adapter` | Add support for a new AI platform |
| `rename-project` | Fork & fully rename OMNISKILL for custom use |

Just tell your AI assistant: *"Follow the add-skill skill to create a new skill for [domain]"*

---

## 🎭 Prompt Library

Organized prompt templates in `prompts/`:

| Prompt | Purpose |
| --- | --- |
| `router.md` | Complexity classification system prompt |
| `system.md` | Master OMNISKILL agent identity prompt |
| `shared.md` | Response formatting, citations, error handling |
| `personas/expert.md` | Deep, thorough analysis persona |
| `personas/quick.md` | Concise, fast response persona |
| `personas/teacher.md` | Step-by-step explanatory persona |

---

## 🐍 Python SDK

```python
from sdk.omniskill import OmniSkill

os = OmniSkill()
os.list_skills(tags=["web"])          # Filter skills by tag
os.route("build a React dashboard")  # Complexity routing
os.install(platform="cursor")        # Install to platform
os.sync_sources()                    # Sync knowledge sources
os.health_check()                    # Comprehensive diagnostics

# v2.0 Pipeline Methods
os.execute_pipeline("sdd-pipeline", project_name="myapp")
os.get_pipeline_status(pipeline_id)
os.resume_pipeline(pipeline_id)
os.list_active_pipelines()
os.cancel_pipeline(pipeline_id)

# v2.0 Synapse Methods
os.list_synapses()                   # All registered synapses
os.get_core_synapses()               # Core synapses only

# v3.0 Session & Policy Methods
from src.omniskill.core.session_manager import Session
session = Session.create("build auth system", "sdd-pipeline")
session.activate()
session.send("spec-step", {"status": "completed"})
session.link_pipeline_trace(pipeline_id)

from src.omniskill.core.policy_engine import PolicyEngine, PermissionRule
engine = PolicyEngine()
engine.add_rule(PermissionRule(id="allow-read", scope="tool", trust_tier="community", action="allow"))
decision = engine.evaluate("Read", session.session_id, session.correlation_id)

from src.omniskill.core.telemetry import TelemetryCollector, ReplayHarness
collector = TelemetryCollector()
collector.emit_from_session_event(session.event_log[-1])
harness = ReplayHarness()
snapshot = harness.capture(session.to_dict(), collector, [])
```

---

## 📖 Documentation

**🌐 [Browse the Full Documentation Site →](https://sufficientdaikon.github.io/omniskill/docs/html/index.html)**

| Guide | Description |
| --- | --- |
| [Getting Started](docs/getting-started.md) | Installation, setup, your first skill |
| [Creating Skills](docs/creating-skills.md) | Skill anatomy, manifest, SKILL.md authoring |
| [Creating Bundles](docs/creating-bundles.md) | Domain kits with meta-skill routing |
| [Creating Agents](docs/creating-agents.md) | Agent personas, skill bindings, handoffs |
| [Creating Pipelines](docs/creating-pipelines.md) | Multi-agent workflows with branching |
| [Creating Synapses](docs/creating-synapses.md) | Custom cognitive capabilities |
| [Platform Guide](docs/platform-guide.md) | Claude Code, Copilot, Cursor, Windsurf, Antigravity |
| [CLI Guide](docs/cli-guide.md) | Full CLI command reference |
| [Architecture](docs/architecture.md) | 6-Layer design, data flow, validation |
| [Guardrails](docs/guardrails.md) | Guardrails engine, Iron Laws, deviation protocol |
| [Sequential Thinking](docs/sequential-thinking.md) | Chain-of-thought protocol, decomposition patterns |
| [Pipeline Orchestration](docs/pipeline-orchestration.md) | Real execution engine, state persistence, context curation |
| [Migration Guide (v2.0)](docs/migration-v2.md) | Upgrading from v0.x to v2.0 |
| [Migration Guide (v3.0)](docs/migration-v3.md) | Upgrading from v2.0 to v3.0 |
| [Agent Cards](docs/agent-cards.md) | Machine-readable agent metadata |
| [MCP Integration Catalog](docs/integration-catalog.md) | 20 curated MCP servers |
| [FAQ](docs/faq.md) | Common questions answered |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding skills, bundles, agents, pipelines, synapses, and hooks.

---

## License

MIT © [SufficientDaikon](https://github.com/SufficientDaikon)
