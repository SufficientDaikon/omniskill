# Glossary

| Term | Definition |
|------|-----------|
| **Skill** | A self-contained unit of AI agent capability. Contains SKILL.md (instructions), manifest.yaml (metadata), and optional resources/overrides/tests/examples. Skills are the atomic building blocks of OMNISKILL. |
| **Bundle** | A domain-specific kit grouping related skills. E.g., `godot-kit` bundles 5 Godot skills. Defined in `bundles/<name>/bundle.yaml`. |
| **Agent** | A formal persona with skill bindings, guardrails, and handoff protocols. Agents execute pipeline steps. Defined in `agents/<name>/AGENT.md` + `agent-manifest.yaml`. |
| **Pipeline** | A multi-agent workflow defined in YAML. Chains agents in sequence with failure recovery. E.g., `sdd-pipeline`: spec-writer → context-curator → implementer → reviewer. |
| **Synapse** | A cognitive capability that shapes HOW agents think, not WHAT they do. Three types: core (always-on), cross-cutting (task-specific), optional (explicitly bound). |
| **Guardrail** | A constraint on agent behavior. Two kinds: `must-do` (required actions) and `must-not` (forbidden actions). Each rule has a severity (critical/major/minor). |
| **Hook** | A lifecycle event handler that fires during pipeline execution. 5 hooks: session_start, pre_step, post_step, on_failure, on_deviation. |
| **Adapter** | A platform-specific strategy for transforming and installing skills. 5 adapters: claude-code, copilot-cli, cursor, windsurf, antigravity. |
| **Manifest** | A YAML metadata file describing a component. Skills use `manifest.yaml`, agents use `agent-manifest.yaml`, bundles use `bundle.yaml`. |
| **Registry** | The `omniskill.yaml` file + the `Registry` Python class that loads and caches all component metadata. Single source of truth. |
| **Pipeline State** | JSON-persisted execution state of a pipeline run. Tracks status, completed steps, accumulated context, deviations, health score. |
| **Session** | A v3 concept extending pipeline state with enforced state machine (8 states), correlation IDs, recovery policies, and event logging. |
| **Policy Engine** | v3 rule-based access control system. Evaluates tool invocations against permission rules, produces immutable `PolicyDecision` artifacts. Default-deny. |
| **Agent Card** | Machine-readable metadata about an agent's capabilities, input/output modes, cost tier, and quality metrics. |
| **Iron Laws** | 10 anti-rationalization rules from the anti-rationalization synapse. E.g., "NO CODING UNTIL THE PLAN IS WRITTEN AND REVIEWED." |
| **Context Curator** | A special agent/skill that curates handoff context between pipeline steps. Ensures relevant state is passed forward, irrelevant data is trimmed. |
| **Deviation Protocol** | The process when an agent deviates from guardrails: STOP → DOCUMENT → ASK → LOG. Critical deviations escalate immediately. |
| **3-Fix Escape Hatch** | After 3 consecutive failures on the same step, the on_failure hook escalates to human review, reasoning that the problem is architectural. |
| **Trust Tier** | Policy engine hierarchy: builtin > verified > community > untrusted. Determines what actions a component is allowed to perform. |
| **SDD** | Spec-Driven Development — the primary workflow methodology. Spec → Implement → Review with context curation between each phase. |
| **MCP** | Model Context Protocol — a standard for AI tool integrations. OMNISKILL has a catalog of 20 curated MCP servers. |
| **Complexity Router** | P0 priority skill that classifies tasks by complexity (TRIVIAL→SIMPLE→MODERATE→COMPLEX→EXPERT) and routes to optimal model/agent. |
| **Gold vs Stub** | Skill quality tiers. "Gold" skills have full Identity/Workflow/Rules/Output/Handoff sections. "Stub" skills are reference-only or missing required sections. |
