# ReverseX - Reverse-Thinking Framework
# Work backwards from the answer to solve complex problems

from typing import Callable, Any

class ReverseEngineer:
    """
    Reverse-thinking problem solver.
    
    Instead of: "What causes X?" → "What must be true if X is true?"
    
    Process:
    1. Define target outcome
    2. Map backwards: what conditions must exist?
    3. Identify blockers: what could prevent these?
    4. Design interventions
    """

    def __init__(self):
        self.traces = []

    def reverse(self, goal: str, context: str = "") -> dict:
        """
        Main reverse-thinking engine.
        
        Args:
            goal: The desired outcome
            context: Background information
        
        Returns:
            Dictionary with conditions, blockers, and path
        """
        conditions = self._derive_conditions(goal)
        blockers = self._find_blockers(conditions)
        path = self._design_path(conditions, blockers)
        
        return {
            "goal": goal,
            "necessary_conditions": conditions,
            "potential_blockers": blockers,
            "action_path": path,
            "confidence": 0.75
        }

    def _derive_conditions(self, goal: str) -> list[str]:
        """Derive conditions that must be true for goal."""
        # Simplified: extract key requirements
        words = goal.split()
        conditions = []
        for i, word in enumerate(words):
            if word.lower() in ["need", "must", "should", "require"]:
                if i + 1 < len(words):
                    conditions.append(" ".join(words[i+1:]))
        if not conditions:
            conditions = [f"Achieve: {goal}"]
        return conditions

    def _find_blockers(self, conditions: list[str]) -> list[str]:
        """Find what could prevent each condition."""
        blockers = []
        for cond in conditions:
            if "knowledge" in cond.lower():
                blockers.append("Insufficient domain knowledge")
            if "skill" in cond.lower():
                blockers.append("Missing required skill")
            if "resource" in cond.lower():
                blockers.append("Insufficient resources")
            if "time" in cond.lower():
                blockers.append("Time constraints")
        return blockers or ["Unknown obstacles"]

    def _design_path(self, conditions: list, blockers: list) -> list[dict]:
        """Design intervention path to overcome blockers."""
        path = []
        for i, (cond, block) in enumerate(zip(conditions, blockers)):
            path.append({
                "step": i + 1,
                "condition": cond,
                "blocker": block,
                "action": f"Address: {block}"
            })
        return path


class ForwardValidator:
    """Validate forward progress after reverse planning."""
    
    def __init__(self):
        self.checkpoints = []

    def add_checkpoint(self, label: str, test: Callable):
        self.checkpoints.append({"label": label, "test": test})

    def validate(self) -> dict:
        results = []
        for cp in self.checkpoints:
            try:
                passed = cp["test"]()
                results.append({"checkpoint": cp["label"], "passed": passed})
            except Exception as e:
                results.append({"checkpoint": cp["label"], "passed": False, "error": str(e)})
        return {
            "passed": all(r["passed"] for r in results),
            "checkpoint_results": results
        }


if __name__ == "__main__":
    solver = ReverseEngineer()
    result = solver.reverse("Need to build a self-improving AI system")
    print("Reverse analysis:", result)