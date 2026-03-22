# Conventions

## Python Conventions

### Naming
| Convention | Style | Consistency |
|-----------|-------|-------------|
| Variables | `snake_case` | 100% |
| Functions | `snake_case` | 100% |
| Classes | `PascalCase` | 100% |
| Constants | `UPPER_SNAKE` | 95% (`OMNISKILL_ROOT`) |
| Private methods | `_leading_underscore` | 100% |
| Modules | `snake_case` | 100% |
| CLI commands | `kebab-case` | 100% (via Typer) |

### Import Ordering
Pattern observed across all source files:
1. `from __future__ import annotations` (first line in every module)
2. Standard library imports (`pathlib`, `json`, `uuid`, `datetime`, `enum`, `re`)
3. Third-party imports (`yaml`, `typer`, `rich`)
4. Internal imports (`from omniskill.core.registry import Registry`)

**Consistency:** ~95% — one deviation at `registry.py:376` where `import os` is at file end with a `noqa: E402` comment to avoid circular imports.

### Type Hints
- **Style:** Python 3.10+ union syntax (`X | None`) enabled via `from __future__ import annotations`
- **Coverage:** ~90% of function signatures have type hints
- **Return types:** Consistently annotated (`-> dict`, `-> None`, `-> list[str]`)
- **Generic types:** `list[str]`, `dict[str, Any]` (lowercase generics, Python 3.9+)

### Docstrings
- **Format:** Google-style with Args/Returns sections
- **Coverage:** ~70% of public functions have docstrings
- **Module-level:** Every module has a docstring explaining purpose and FR/E references

### Code Organization
Every Python file follows this structure:
1. Module docstring (with requirement references like FR-062, E2-S1)
2. Future imports
3. Standard library imports
4. Third-party imports
5. Constants (e.g., `OMNISKILL_ROOT`)
6. Dataclass definitions
7. Main class(es)
8. Helper functions (private)

## YAML Conventions

### Skill Manifests (manifest.yaml)
| Field | Required | Format |
|-------|----------|--------|
| `name` | Yes | kebab-case |
| `version` | Yes | semver (MAJOR.MINOR.PATCH) |
| `description` | Yes | String, max 200 chars (often exceeded) |
| `author` | Yes | String |
| `license` | Yes | SPDX identifier |
| `platforms` | Yes | Array of platform IDs |
| `tags` | Yes | Array of lowercase kebab-case strings |
| `triggers.keywords` | Yes | Array of trigger phrases |
| `triggers.patterns` | Optional | Array of glob patterns |
| `priority` | Optional | P0-P4 scale |

**Consistency issues:** Many skills (especially stub/dissected ones) are missing required fields like `author`, `platforms`, `triggers`, `priority`. The validate command reports 63 failures.

### Agent Manifests (agent-manifest.yaml)
Required fields per schema: `name`, `version`, `role`, `description`, `persona`, `skill-bindings`, `input-contract`, `output-contract`, `guardrails`, `guardrail-enforcement`.

**Consistency issues:** Most agents (8/9) are missing `persona`, `skill-bindings`, `input-contract`, `output-contract` fields.

### Skill Names
- Always `kebab-case` (e.g., `react-best-practices`, `godot-gdscript-mastery`)
- Descriptive compound names preferred
- Domain prefix for grouped skills (e.g., `godot-*`, `django-*`, `ux-*`)

## Markdown Conventions

### SKILL.md Structure (Gold Standard)
Skills following the template have these sections:
1. `## Identity` — Agent persona name and description
2. `## When to Use` — Trigger conditions with keywords
3. `## Workflow` — Step-by-step process
4. `## Rules` — DO/DON'T lists
5. `## Output Format` — Expected output structure
6. `## Handoff` — Next agent/skill in chain
7. `## Platform Notes` — Platform-specific behavior

**Reality:** Only ~30% of skills follow this full structure. Many are reference-style documents or use custom section structures.

### Three SKILL.md Patterns Observed
1. **Standard Template** (~25 skills): Identity/Workflow/Rules/Output Format/Handoff
2. **Pure Reference** (~40 skills): Frontmatter + dense reference content, no workflow
3. **Custom Process** (~18 skills): Non-standard sections (Iron Laws, Rationalization Tables)
