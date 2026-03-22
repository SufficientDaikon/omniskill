# Code Examples

## 1. Using the SDK

```python
from sdk.omniskill import OmniSkill

# Initialize
os = OmniSkill()

# List all skills
skills = os.list_skills()
print(f"Found {len(skills)} skills")

# Filter by tags
godot_skills = os.list_skills(tags=['godot'])

# Get skill details
skill = os.get_skill('complexity-router')
print(skill['manifest']['name'])
print(skill['content'][:200])  # First 200 chars of SKILL.md

# Health check
health = os.health_check()
print(f"Status: {health['status']}, Skills: {health['skills_count']}")

# Route a query
route = os.route("Build a complex authentication system with OAuth2")
print(f"Classification: {route['classification']}")  # COMPLEX
print(f"Execution mode: {route['execution_mode']}")  # agent
```

## 2. Running a Pipeline

```python
from sdk.omniskill import OmniSkill

os = OmniSkill()

# Execute sdd-pipeline
result = os.execute_pipeline('sdd-pipeline', project_dir='./myapp')
print(f"Status: {result['status']}")

# Check active pipelines
active = os.list_active_pipelines()
for p in active:
    print(f"  {p['pipeline']}: {p['status']}")

# Resume a failed pipeline
if result['status'] == 'failed':
    resumed = os.resume_pipeline(result['state_id'])
```

## 3. Using the Registry Directly

```python
from omniskill.core.registry import Registry

reg = Registry()
reg.load()

# Find a skill
skill = reg.find_skill('implementer')
print(f"Skill: {skill.name}, Priority: {skill.priority}")

# Load full manifest
manifest = reg.load_skill_manifest(skill)
print(f"Platforms: {skill.platforms}")
print(f"Tags: {skill.tags}")

# Fuzzy search
matches = reg.similar_names('godot')
print(f"Similar: {matches}")  # ['godot-best-practices', 'godot-debugging', ...]
```

## 4. Using the Pipeline Engine

```python
from omniskill.core.pipeline_engine import PipelineExecutor, StepResult, StepStatus

executor = PipelineExecutor()
pipeline = executor.load_pipeline('sdd-pipeline')

# Custom step handler
def my_handler(step_config, context):
    print(f"Executing: {step_config['name']} with agent {step_config['agent']}")
    return StepResult(
        step_name=step_config['name'],
        status=StepStatus.COMPLETED,
        artifacts=['output.md'],
    )

result = executor.execute(pipeline, step_handler=my_handler)
```

## 5. Using the Policy Engine

```python
from omniskill.core.policy_engine import PolicyEngine, PermissionRule

engine = PolicyEngine()

# Add a rule
engine.add_rule(PermissionRule(
    id="allow-read",
    scope="tool",
    trust_tier="community",
    action="allow",
))

# Evaluate
decision = engine.evaluate(
    tool_name="read_file",
    session_id="sess-abc123",
    correlation_id="corr-xyz",
    arguments={"path": "/tmp/test.txt"},
)

print(f"Action: {decision.action}")  # allow
print(f"Rationale: {decision.rationale}")

# Audit log
for d in engine.audit_log:
    print(f"  {d.tool_name}: {d.action}")
```

## 6. Using the Session Manager

```python
from omniskill.core.session_manager import Session

# Create session
session = Session.create(
    objective="Build authentication feature",
    pipeline_name="sdd-pipeline",
)
print(f"Session: {session.session_id}")
print(f"Status: {session.status.value}")  # created

# Activate and work
session.activate()
session.send("spec-writing", {"status": "completed", "artifacts": ["spec.md"]})
session.add_decision("Using JWT for auth tokens")

# Save to disk
path = session.save()
print(f"Saved to: {path}")

# Integrity check
checksum = session.context_checksum()
print(f"Checksum: {checksum}")
```

## 7. Creating a Minimal Skill

```yaml
# skills/my-skill/manifest.yaml
name: my-skill
version: 1.0.0
description: "Use when building XYZ features"
author: your-name
license: MIT
platforms: [claude-code, copilot-cli, cursor, windsurf, antigravity]
tags: [my-domain, specific-tag]
triggers:
  keywords: ["xyz", "my feature"]
  patterns: ["build * xyz*", "create * xyz*"]
priority: P2
```

```markdown
<!-- skills/my-skill/SKILL.md -->
## Identity
You are the **XYZ Specialist** — an expert in building XYZ features.

## When to Use
Use this skill when the user asks to build, modify, or debug XYZ features.

## Workflow
1. **Analyze** — Understand the XYZ requirement
2. **Design** — Plan the implementation approach
3. **Implement** — Build the feature
4. **Validate** — Verify against requirements

## Rules
**DO:**
- Follow the established XYZ patterns
- Write tests for all new code

**DON'T:**
- Skip validation steps
- Modify unrelated code

## Output Format
Deliver: implementation code + test file + brief summary.

## Handoff
Next agent: `reviewer` for compliance check.
```
