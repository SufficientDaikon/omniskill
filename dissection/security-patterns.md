# Security Patterns

## Security Infrastructure

### 1. Policy Engine (`core/policy_engine.py`)
- **Default-deny policy:** If no rule matches, access is denied
- **Trust tier hierarchy:** `builtin > verified > community > untrusted`
- **Schema validation before invocation:** Tool arguments validated against registered schemas
- **Immutable audit trail:** Every policy decision recorded with decision_id, timestamp, rationale
- **Replayable decisions:** `get_decisions_for_session()` enables forensic replay

### 2. Security-Awareness Synapse (`synapses/security-awareness/`)
- Cross-cutting synapse that injects OWASP security checks during code tasks
- SCAN → FLAG phases for automated security review
- Note: Missing required manifest fields (synapse-type, firing-phases, tags)

### 3. Guard-Chain Skill (`skills/guard-chain/`)
- Auth middleware patterns for API routes
- Authentication → Authorization → Rate Limiting → Input Validation chain

### 4. Guardrail System
- Every agent has `guardrails.must-do` and `guardrails.must-not` rules
- `guardrail-enforcement: strict` flag enforces halt on violation
- 15 schema files validate component structure

## Input Validation

| Surface | Validation | Quality |
|---------|-----------|---------|
| CLI arguments | Typer type checking (built-in) | Good |
| YAML manifests | SchemaValidator with field/type/pattern checks | Good |
| Pipeline YAML | PipelineDefinition.from_yaml with field defaults | Minimal |
| Tool invocations (v3) | PolicyEngine.evaluate() with argument schemas | Good |
| User input in SDK | Basic type/None checks | Minimal |

## YAML Security
- **All YAML loading uses `yaml.safe_load()`** — no `yaml.load()` with arbitrary constructors
- This prevents YAML deserialization attacks (arbitrary code execution)
- Consistent across all 33 YAML read locations

## Secret Handling
- **No hardcoded secrets found** in source code
- No API keys, tokens, or passwords in any Python file
- `.gitignore` properly excludes sensitive patterns
- Environment variable `OMNISKILL_ROOT` used for path configuration (not secrets)

## File System Safety
- Path construction uses `pathlib.Path` throughout (no string concatenation)
- `Path.expanduser()` used safely for `~` expansion
- `mkdir(parents=True, exist_ok=True)` prevents race conditions
- No `os.system()` or `subprocess.run()` with shell=True in core code

## Identified Gaps

1. **No authentication for SDK operations** — anyone who can import the SDK can install/modify skills
2. **No integrity verification** — no checksums/signatures on skill files
3. **Dependency vulnerabilities unknown** — no `pip audit` or dependency scanning configured
4. **No rate limiting** on pipeline execution
5. **Session state stored as plain JSON** — no encryption at rest
