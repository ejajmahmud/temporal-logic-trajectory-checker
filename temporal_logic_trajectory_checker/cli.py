"""CLI for temporal-logic-trajectory-checker."""
import sys
import argparse
from .checker import TemporalLogicTrajectoryChecker


def main():
    parser = argparse.ArgumentParser(description="Temporal Logic Trajectory Checker CLI")
    parser.add_argument("--demo", action="store_true", help="Run temporal logic verification demo")
    args = parser.parse_args()

    if args.demo:
        checker = TemporalLogicTrajectoryChecker()
        checker.record_step(["authorized", "idle"])
        checker.record_step(["authorized", "compiling"])
        checker.record_step(["authorized", "tested", "goal_achieved"])

        safe = checker.check_always("authorized")
        live = checker.check_eventually("goal_achieved")
        print(f"[*] Trajectory Safety (Always authorized): {safe}")
        print(f"[*] Trajectory Liveness (Eventually goal_achieved): {live}")
    else:
        parser.print_help()
    sys.exit(0)


if __name__ == "__main__":
    main()
