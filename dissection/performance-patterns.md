# Performance Patterns

## Registry Loading
- **Strategy:** Lazy loading with `ensure_loaded()` guard
- **Behavior:** First access triggers full `omniskill.yaml` parse; subsequent lookups use cached lists
- **Manifest backfill:** Individual component manifests loaded on demand (not eagerly)
- **Assessment:** Good for CLI startup; ~83 skill entries parsed from a single YAML file

## Pipeline Execution
- **Strategy:** Synchronous, sequential step execution
- **No async/await:** Zero `async` usage in the entire codebase
- **Timing:** Each step measured with `time.time()` for duration_ms tracking
- **State persistence:** JSON serialized to disk after every step (safe but I/O heavy)
- **Assessment:** Adequate for the intended use case (AI agent orchestration where each step is long-running)

## File I/O Patterns
| Pattern | Frequency | Quality |
|---------|-----------|---------|
| `open(path, "r", encoding="utf-8")` | ~30 instances | Good — consistent UTF-8 |
| `pathlib.Path.read_text()` | ~5 instances | Good — simpler syntax |
| `json.dump()` with indent=2 | ~5 instances | Fine for debug; slightly larger files |
| `yaml.safe_load()` | ~33 instances | Good — no streaming needed for small files |

## Memory Patterns
- All component data loaded as Python dicts/dataclasses (in-memory)
- No explicit caching layer beyond the Registry's `_loaded` flag
- No memory profiling or limits configured
- SDK `list_skills()` reads all manifest.yaml files on every call (no caching)

## Search Performance
- `Registry.find_skill()` is O(n) linear scan over skill list
- `similar_names()` is O(n) with string comparison per component
- For 83 skills, this is negligible (<1ms)
- No indexing or hash-based lookup (not needed at current scale)

## Bottleneck Analysis

| Area | Current | Impact | Suggestion |
|------|---------|--------|-----------|
| Registry loading | Single YAML parse | Low — fast for 83 skills | Fine as-is |
| Manifest backfill | Per-file YAML reads | Medium — 83 files if loading all | Consider batch loading |
| Pipeline state I/O | JSON write per step | Low — steps are long-running | Fine as-is |
| SDK skill listing | Re-reads all manifests | Medium — no cache between calls | Add timestamp-based cache |
| Validation | Sequential file reads | Medium — 113 components checked | Could parallelize |

## No Async Architecture
The entire codebase is synchronous Python. This is appropriate because:
1. The primary consumer is CLI (inherently sequential)
2. Pipeline steps represent AI agent work (long-running, not I/O-bound)
3. File operations are local and fast
4. No network calls in the core library
