# ReverseX User Guide

> Reverse-Thinking Problem Solver — Work Backward from Goals to Make the Impossible Possible

---

## Core Concept

ReverseX is a **reverse reasoning framework** that flips traditional "from known to unknown" forward thinking on its head, using a "work backward from goals to find what conditions are needed" reverse approach to problem-solving.

**Why does it matter?**

Traditional AI problem-solving is linear and forward:
```
Known condition A → Reasoning B → Reasoning C → Conclusion D
```

This approach easily falls into these traps with complex problems:
- Intermediate step explosion — long reasoning chains accumulate errors
- Local optimum but global sub-optimum
- Misled by false premises, reasoning gets further and further off track

ReverseX's core approach:
```
Goal Z → What conditions are needed? → How to satisfy these conditions? → Trace back to known
```

This approach excels at solving:
- "How do I achieve X?" type problems
- Creative generation and solution design
- Counterfactual reasoning
- Path planning and resource optimization

---

## How to Use

### Step 1: Define the Goal

```python
from reversex import ReverseEngine, Goal

# Define a clear goal
goal = Goal(
    target="Launch product within 6 months",
    constraints=["Budget: 500K", "Team: 5 people", "Must support iOS and Android"],
    success_criteria="Monthly active users exceed 10K"
)
```

### Step 2: Trigger Reverse Analysis

```python
engine = ReverseEngine()

# Work backward from the goal
result = await engine.analyze(goal)

print(result.pathway)
# Output:
# Goal: Launch in 6 months
#   └ Requires: MVP completion → Requires: Core feature development (3 months) + UI design (1 month) + Testing (1 month)
#       └ Requires: Technology selection → Choose: Cross-platform framework (Flutter/React Native) over native development
#           └ Requires: Build/outsource decision → Choose: Hybrid strategy (3 internal + 2 outsourced)
```

### Step 3: Obtain Action Paths

```python
# Get complete reverse derivation results
analysis = await engine.analyze(goal)

for step in analysis.decompose():
    print(f"Stage: {step.name}")
    print(f"  Prerequisites: {step.requirements}")
    print(f"  Execution Strategy: {step.strategy}")
    print(f"  Validation Method: {step.validation}")

# Output includes:
# - Complete condition tree
# - Feasible paths for each node
# - Key milestones
# - Risk points and backup plans
```

---

## Code Example

```python
import asyncio
from reversex import ReverseEngine, Goal, NodeType

async def solve_problem():
    engine = ReverseEngine(depth_limit=10)

    # Case: How to build an AI Agent system
    goal = Goal(
        target="Build an enterprise AI Agent system",
        constraints=[
            "Support 10+ tool calls",
            "Latency below 500ms",
            "High observability",
            "Monthly cost under 50K"
        ]
    )

    result = await engine.analyze(goal)

    # Print the reverse derivation path diagram
    result.print_tree()

    # Get key decision points
    decisions = result.get_critical_decisions()
    for d in decisions:
        print(f"\nKey Decision: {d.question}")
        print(f"  Option A: {d.option_a}")
        print(f"  Option B: {d.option_b}")
        print(f"  Recommendation: {d.recommendation}")

    return result.action_plan

asyncio.run(solve_problem())
```

---

## Use Cases

### Case 1: Technical Solution Design
When you need to design a complex system, ReverseX can work backward from "what effects should the system achieve" to determine "what architecture is needed." For example: from "support 1 million concurrent users" derive what kind of database, middleware, and caching strategy is needed.

### Case 2: Business Model Innovation
"How do we grow annual revenue beyond 100 million?" ReverseX breaks this down: what products, customers, pricing strategy, and channels are needed, tracing back to the first step you can start executing today.

### Case 3: Root Cause Analysis of Failures
"Why did this service outage happen?" Forward analysis requires checking all possible causes. ReverseX works backward from "service outage" as the result: what upstream failure could cause this? What deeper cause could lead to the upstream failure?

### Case 4: Resource Optimization
"How do we maximize technical value within a limited budget?" ReverseX traces back from the target effect to prioritize resource allocation, helping decision-makers find the optimal solution under constraints.

---

## Relationship with Other Modules

| Module | Relationship | Description |
|:----:|:----:|:-----|
| NexusCore | Reasoning Execution | ReverseX analysis results are executed and verified via NexusCore |
| AgentHive | Collaborative Reasoning | Multiple agents in AgentHive can perform distributed reverse reasoning with ReverseX |
| QuantMind | Decision Support | Before QuantMind makes trading decisions, it uses ReverseX to verify strategy feasibility |
| MirrorOS | Shared Reasoning | Multiple MirrorOS instances share the same ReverseX engine |

**Architecture Position**: ReverseX is the reasoning engine, excelling at "how to achieve goals" type problems. It's core support for complex decision-making.

---

## Advanced: Constraint Relaxation

```python
# When a goal cannot be achieved, ReverseX can analyze which constraints can be relaxed
result = await engine.analyze_with_relaxation(
    goal,
    relaxable_constraints=["time", "budget"],
    frozen_constraints=["safety standards", "compliance requirements"]
)

print("Alternative Plans:")
for path in result.alternative_paths:
    print(f"  Plan {path.id}: Relax {path.released_constraints}")
    print(f"    Achievable Goal: {path.achievable_goal}")
    print(f"    Cost: {path.cost}")
```

---

## Next Steps

- See the [QuantMind Guide](./quantmind-guide_en.md) — How to use ReverseX for trading decisions
- See the [AgentHive Guide](./agenthive-guide_en.md) — Multi-agent reverse reasoning collaboration
- Get started: `pip install reversex`

---

*ReverseX — Upgrade thinking from "go with the flow" to "work backward"*
