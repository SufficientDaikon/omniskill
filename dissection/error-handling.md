# Error Handling Patterns

## Custom Exception Classes

| Exception | Location | Purpose |
|-----------|----------|---------|
| `InvalidTransitionError` | `core/session_manager.py:61` | Raised on invalid state machine transitions |

Only 1 custom exception defined. All other error handling uses standard Python exceptions.

## Error Handling Strategies

### 1. Pipeline Failure Recovery (`hooks/on_failure.py`)

The on-failure hook implements a 5-action recovery model:

| Action | When Used | Behavior |
|--------|-----------|----------|
| `retry` | Transient failures, attempt < max_retries | Re-execute same step |
| `loop` | Iterative refinement needed | Send back to earlier step |
| `escalate` | 3+ consecutive failures (escape hatch) | Escalate to human/debugger |
| `halt` | Default, unrecoverable errors | Stop pipeline execution |
| `skip` | Non-critical step failure | Continue to next step |

**3-Fix Escape Hatch:** After 3 failed attempts, the hook automatically escalates, reasoning that repeated failure indicates an architecture problem, not a bug.

### 2. Auto-Recovery Patterns (`hooks/on_failure.py:104`)

Pattern-based error classification:
```python
recovery_patterns = {
    "file not found": {"action": "retry", "fix": "Check file paths"},
    "permission denied": {"action": "halt", "fix": "Fix permissions"},
    "timeout": {"action": "retry", "fix": "Increase timeout"},
    "connection refused": {"action": "retry", "fix": "Check service"},
    "out of memory": {"action": "halt", "fix": "Reduce scope"},
}
```

### 3. Catch Patterns in Source Code

| Pattern | Frequency | Quality |
|---------|-----------|---------|
| `except Exception:` (broad) | ~15 instances | Mixed — used for YAML parsing safety |
| `except (json.JSONDecodeError, KeyError, ValueError):` | 3 instances | Good — specific |
| `except yaml.YAMLError:` | 2 instances | Good — specific |
| `except re.error as e:` | 1 instance | Good — regex validation |

### 4. Deviation Protocol (`hooks/on_deviation.py`)

When agents deviate from their guardrails:
```
STOP → DOCUMENT → ASK → LOG
```
- Critical deviations: escalated immediately
- Non-critical: logged with severity, action continues

### 5. Hook Error Policies

Configured in `hooks/hooks.yaml`:
- `session-start`: `on-error: warn` (non-blocking)
- `pre-step`: `on-error: halt` (blocking)
- `post-step`: `on-error: halt` (blocking)
- `on-failure`: `on-error: halt` (blocking)
- `on-deviation`: `on-error: halt` (blocking)

### 6. Pipeline Engine Error Handling

```python
try:
    step_result = step_handler(step_config, context)
except Exception as e:
    step_result = StepResult(
        step_name=step_name,
        status=StepStatus.FAILED,
        errors=[str(e)],
    )
```

Pattern: Catch-all at pipeline execution boundary, convert exceptions to step results with error details. State is always saved, even on failure.

## Logging Approach

- No structured logging framework (no `logging` module usage in core)
- `print()` with `file=sys.stderr` for warnings in pipeline engine
- Rich console output via `utils/output.py` for user-facing messages
- Hook event log stored in session state (JSON persistence)
