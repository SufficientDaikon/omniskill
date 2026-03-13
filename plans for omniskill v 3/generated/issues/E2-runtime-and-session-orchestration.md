# E2 - Runtime and Session Orchestration

## Priority
`P0`

## Dependencies
E1

## Stories
- [ ] Implement client lifecycle state machine with restart and recovery policies.
- [ ] Implement session lifecycle service with create, resume, send, abort, archive semantics.
- [ ] Link session and pipeline traces with correlation IDs.

## Definition of Done
- [ ] Recovery from controlled crash with trace continuity.
- [ ] No invalid state transition accepted.
- [ ] Session resume preserves active constraints and objective.
