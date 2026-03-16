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
[![Skills](https://img.shields.io/badge/skills-83-blue)]()
[![Bundles](https://img.shields.io/badge/bundles-12-green)]()
[![Agents](https://img.shields.io/badge/agents-10-orange)]()
[![Pipelines](https://img.shields.io/badge/pipelines-8-red)]()
[![Synapses](https://img.shields.io/badge/synapses-5-blueviolet)]()
[![Hooks](https://img.shields.io/badge/hooks-5-yellow)]()
[![Schemas](https://img.shields.io/badge/schemas-15-lightgrey)]()
[![Platforms](https://img.shields.io/badge/platforms-5-purple)]()
[![Tests](https://img.shields.io/badge/tests-500-success)]()

_Write skills once. Run them on Claude Code, Copilot CLI, Cursor, Windsurf, and Antigravity._

**📖 [Browse the Documentation Site →](https://sufficientdaikon.github.io/omniskill/docs/html/index.html)**

</div>

---

## What is OMNISKILL?

OMNISKILL is a **universal framework** for AI coding assistant skills, agents, and workflows. It solves the fragmentation problem: instead of maintaining separate skill files for every AI tool, you write once in a universal format and deploy everywhere.

| Feature | Description |
| --- | --- |
| 🎯 **Universal Skills** | 83 skills in a single format that works on 5 AI platforms |
| 📦 **Bundles** | 12 domain kits (Godot, Web Dev, UX, Django, Security, DevOps...) |
| 🤖 **Formal Agents** | 10 agents with personas, skill bindings, guardrails, and handoff protocols |
| 🔄 **Pipelines** | 8 multi-agent workflows with failure recovery and context curation |
| 🧠 **Synapses** | 5 cognitive capabilities that shape HOW agents think |
| 🛡️ **Guardrails & Hooks** | 5 lifecycle hooks enforcing discipline at runtime |
| 📜 **Runtime Contracts** | Session state machine, central policy engine, telemetry, replay harness |
| 🧪 **500 Tests** | Full test suite with zero regressions across v2→v3 |
| 🔌 **Cross-Platform** | Claude Code, Copilot CLI, Cursor, Windsurf, Antigravity |

---

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/SufficientDaikon/omniskill.git
cd omniskill
```

### 2. Install

```bash
pip install omniskill                              # From PyPI
omniskill init                                     # Auto-detect your AI platforms
omniskill install --all                            # Install all 83 skills
omniskill doctor                                   # Verify everything works
```

Or install manually:

```bash
python scripts/install.py                          # Auto-detects platforms
python scripts/install.py --platform claude-code   # Specific platform
python scripts/install.py --bundle web-dev-kit     # Specific bundle only
```

### 3. Run a Pipeline

```bash
omniskill pipeline run sdd-pipeline --project ./myapp
```

This triggers the full Spec-Driven Development flow: **spec-writer → context-curator → implementer → context-curator → reviewer** with automatic failure recovery.

---

## 🏗️ Architecture

OMNISKILL uses a 6-layer architecture where each layer builds on the one below:

| Layer | What It Does |
| --- | --- |
| **Layer 1 — Skills & Knowledge** | 83 skills, 12 bundles, prompt library, knowledge sources |
| **Layer 2 — Agents & Personas** | 10 agents with formal personas, handoff contracts, and quality gates |
| **Layer 3 — Synapses & Cognition** | 5 cognitive synapses that shape HOW agents reason |
| **Layer 4 — Pipelines & Orchestration** | 8 pipelines with real execution, context curation, failure recovery |
| **Layer 5 — Guardrails & Hooks** | 5 lifecycle hooks enforcing discipline at runtime |
| **Layer 6 — Runtime Contracts** | Session state machine, policy engine, telemetry, MCP trust routing |

```
omniskill/
├── skills/           # 83 skills (SKILL.md + manifest.yaml + resources)
├── bundles/          # 12 domain bundles (bundle.yaml + meta-skill)
├── agents/           # 10 agent definitions (AGENT.md + agent-manifest.yaml)
├── pipelines/        # 8 multi-agent workflows
├── synapses/         # 5 cognitive synapses (SYNAPSE.md + manifest.yaml)
├── hooks/            # 5 lifecycle hooks
├── src/              # Core engine (v3.0 — session, policy, telemetry, replay)
├── prompts/          # Prompt library (router, system, personas)
├── sdk/              # Python SDK
├── adapters/         # 5 platform adapters
├── schemas/          # 15 validation schemas (9 v2 + 6 v3)
├── scripts/          # CLI tools (install, doctor, validate, admin)
├── tests/            # 500 automated tests
└── docs/             # Documentation site + markdown guides
```

---

## 🎯 Skills

83 skills in a universal format. Every skill has:

```
skills/my-skill/
├── SKILL.md           # Instructions (Identity, Workflow, Rules, Output, Handoff)
├── manifest.yaml      # Metadata (triggers, platforms, tags, dependencies)
├── resources/         # Reference materials (cheat sheets, style guides)
├── examples/          # Sample interactions
├── templates/         # Output templates
├── tests/             # Validation test cases
└── overrides/         # Platform-specific overrides
```

Key skills include: `complexity-router` (smart task routing), `context-curator` (pipeline context management), `guard-chain` (auth middleware patterns), `structured-logging` (observability), and 79 more.

See [`skills/_template/`](skills/_template/) for the template.

---

## 📦 Bundles

| Bundle | Skills | Description |
| --- | --- | --- |
| **godot-kit** | 5 | Godot 4 / GDScript development |
| **web-dev-kit** | 10 | Frontend, React, RSC, i18n, error handling, backend |
| **ux-design-kit** | 7 | Full UX pipeline: research → wireframe → visual → test |
| **django-kit** | 4 | Django framework, ORM, REST APIs |
| **sdd-kit** | 6 | Spec-Driven Development: spec → implement → review |
| **testing-kit** | 5 | Unit tests, E2E testing, QA planning, debugging |
| **mobile-kit** | 2 | Mobile design, Capacitor best practices |
| **meta-kit** | 5 | Skill creation, discovery, packaging, prompts |
| **prompts-chat-kit** | 17 | Plugin system, builders, quality gates, webhooks, SDK |
| **security-kit** | 4 | Guard chain, webhooks, error handling, logging |
| **data-layer-kit** | 4 | Prisma ORM, singletons, deduplication, backend |
| **devops-kit** | 2 | Docker production builds, structured logging |

---

## 🤖 Agents

| Agent | Role | Primary Skills |
| --- | --- | --- |
| spec-writer-agent | Specification Architect | spec-writer, prompt-architect |
| implementer-agent | Implementation Engineer | implementer |
| reviewer-agent | Compliance Reviewer | reviewer |
| debugger-agent | Debug Investigator | systematic-debugging |
| context-curator-agent | Context Architect | context-curator |
| dissector-agent | Codebase Analyst | knowledge-sources |
| ux-research-agent | UX Researcher | ux-research |
| ui-design-agent | Visual Designer | ui-visual-design, frontend-design |
| qa-master-agent | QA Engineer | e2e-testing-patterns, qa-test-planner |
| security-reviewer-agent | Security Auditor | guard-chain, error-handling-architecture |

Every agent has guardrails (`guardrail-enforcement: strict`), skill bindings, and handoff protocols. Run `omniskill cards` for machine-readable agent cards.

---

## 🔄 Pipelines

| Pipeline | Flow | Trigger |
| --- | --- | --- |
| **sdd-pipeline** | spec-writer → context-curator → implementer → context-curator → reviewer | "build feature X from scratch" |
| **ux-pipeline** | research → context-curator → wireframe → visual → review → handoff | "design feature X" |
| **debug-pipeline** | debug → context-curator → implement → test → review | "fix bug X" |
| **skill-factory** | prompt → spec → context-curator → implement → validate → review | "create a new skill for X" |
| **full-product** | ux-pipeline → context-curator → sdd-pipeline → testing | "build product X end-to-end" |
| **godot-pipeline** | design → implement → test → review | "build Godot feature X" |
| **dissect-to-skill** | dissect → diff → specify → implement → validate → register | "dissect codebase X into skills" |
| **skill-upgrade** | assess → specify-upgrade → rewrite → verify | "upgrade stub skill to gold" |

Pipelines are **resumable** — if interrupted, they save state and continue from the last completed step.

---

## 🧠 Synapses

Synapses are **cognitive capabilities** that shape HOW agents think, not WHAT they do.

| Synapse | Type | Phases | Description |
| --- | --- | --- | --- |
| **metacognition** | core | PLAN → MONITOR → REFLECT | Structured self-awareness: plan before acting, tag confidence |
| **anti-rationalization** | core | DETECT → CHALLENGE → ENFORCE | Prevents excuse-making via 10 Iron Laws |
| **sequential-thinking** | core | DECOMPOSE → REASON → VALIDATE → SYNTHESIZE | Step-by-step task decomposition |
| **security-awareness** | cross-cutting | SCAN → FLAG | Injects OWASP security checks during code tasks |
| **pattern-recognition** | optional | DETECT → SUGGEST → APPLY | Scans code for patterns, surfaces matching skills |

**Core** synapses fire automatically for every agent. **Cross-cutting** fire for specific task types. **Optional** require explicit binding.

---

## 🔌 Supported Platforms

| Platform | Adapter | Target Location |
| --- | --- | --- |
| Claude Code | `adapters/claude-code/` | `~/.claude/skills/` |
| GitHub Copilot CLI | `adapters/copilot-cli/` | `~/.copilot/skills/` |
| Cursor | `adapters/cursor/` | `.cursor/rules/` |
| Windsurf | `adapters/windsurf/` | `.windsurfrules` |
| Antigravity | `adapters/antigravity/` | `.antigravity/skills/` |

---

## 📖 Documentation

**📖 [Browse the Full Documentation Site →](https://sufficientdaikon.github.io/omniskill/docs/html/index.html)**

| Guide | Description |
| --- | --- |
| [Getting Started](docs/getting-started.md) | Installation, setup, your first skill |
| [Creating Skills](docs/creating-skills.md) | Skill anatomy, manifest, SKILL.md authoring |
| [Creating Bundles](docs/creating-bundles.md) | Domain kits with meta-skill routing |
| [Creating Agents](docs/creating-agents.md) | Agent personas, skill bindings, handoffs |
| [Creating Pipelines](docs/creating-pipelines.md) | Multi-agent workflows with branching |
| [Creating Synapses](docs/creating-synapses.md) | Custom cognitive capabilities |
| [Platform Guide](docs/platform-guide.md) | Platform-specific setup details |
| [CLI Guide](docs/cli-guide.md) | Full CLI command reference |
| [Architecture](docs/architecture.md) | 6-Layer design, data flow, validation |
| [Guardrails](docs/guardrails.md) | Guardrails engine, Iron Laws, deviation protocol |
| [Sequential Thinking](docs/sequential-thinking.md) | Chain-of-thought protocol |
| [Pipeline Orchestration](docs/pipeline-orchestration.md) | Execution engine, state persistence |
| [DDE Methodology](docs/DDE-METHODOLOGY.md) | Dissection-Driven Enhancement process |
| [Agent Cards](docs/agent-cards.md) | Machine-readable agent metadata |
| [MCP Integration Catalog](docs/integration-catalog.md) | 20 curated MCP servers |
| [Migration Guide (v2)](docs/migration-v2.md) | Upgrading from v0.x to v2.0 |
| [Migration Guide (v3)](docs/migration-v3.md) | Upgrading from v2.0 to v3.0 |
| [FAQ](docs/faq.md) | Common questions answered |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding skills, bundles, agents, pipelines, synapses, and hooks.

---

## License

MIT © [SufficientDaikon](https://github.com/SufficientDaikon)
