"""Core Temporal Logic Trajectory Checker implementation."""
from typing import List, Dict, Set, Optional, Any


class TraceEvent:
    def __init__(self, step_idx: int, predicates: Set[str], payload: Optional[Dict[str, Any]] = None):
        self.step_idx = step_idx
        self.predicates = set(predicates)
        self.payload = payload or {}


class TemporalLogicTrajectoryChecker:
    def __init__(self):
        self.events: List[TraceEvent] = []

    def record_step(self, predicates: List[str], payload: Optional[Dict[str, Any]] = None):
        idx = len(self.events)
        self.events.append(TraceEvent(idx, set(predicates), payload))

    def check_always(self, predicate: str) -> bool:
        """Globally (G p): predicate must hold at every state in the trajectory."""
        if not self.events:
            return True
        return all(predicate in ev.predicates for ev in self.events)

    def check_eventually(self, predicate: str) -> bool:
        """Eventually (F p): predicate must hold at at least one state in the trajectory."""
        return any(predicate in ev.predicates for ev in self.events)

    def check_until(self, p1: str, p2: str) -> bool:
        """Until (p1 U p2): p1 holds until p2 holds."""
        for ev in self.events:
            if p2 in ev.predicates:
                return True
            if p1 not in ev.predicates:
                return False
        return False
