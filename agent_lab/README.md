# Agent Workbench

The Agent Workbench is the practical control plane for the agent-native part of the course.

It is deliberately vendor-neutral and deterministic. The purpose is to teach the engineering controls around an agent—context, tools, permissions, verification and evidence—without making a particular model provider the curriculum dependency.

## Work contract

Every delegated task starts with:

```text
Goal
Context
Constraints
Tools
Permissions
Success criteria
Failure conditions
Evidence required
Escalation policy
```

See `context/agent_work_contract.md`.

## Permission ladder

| Level | Agent may | Human responsibility |
|---|---|---|
| 0 | Explain | Define the question |
| 1 | Inspect | Decide what context is trustworthy |
| 2 | Propose | Judge the proposed plan |
| 3 | Modify sandbox | Bound the blast radius |
| 4 | Run tests | Inspect evidence |
| 5 | Create PR | Review the change |
| 6 | Deploy with approval | Approve the release |
| 7 | Bounded production action | Define and audit the policy |

The demo harness defaults to **Level 2**. A higher level must be explicitly granted by policy.

## Workflow

```text
Specify → Delegate → Inspect → Verify → Challenge → Decide
                 ↑                         ↓
              Trace                    Eval / attack
```

## What to inspect

- `tools/tool_gateway.py` — bounded tool interface
- `policies/permissions.json` — permission policy
- `traces/example_trace.json` — inspectable agent trace
- `evals/cases.json` — repeatable evaluation cases
- `attacks/` — adversarial inputs
- `graders/grade_trace.py` — deterministic policy/evidence grader
- `run_demo.py` — end-to-end deterministic demonstration

The workbench is an engineering laboratory, not a production agent runtime.
