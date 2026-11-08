"""Unit tests for temporal-logic-trajectory-checker."""
import unittest
from temporal_logic_trajectory_checker.checker import TemporalLogicTrajectoryChecker


class TestTemporalLogicTrajectoryChecker(unittest.TestCase):
    def test_always_property(self):
        c = TemporalLogicTrajectoryChecker()
        c.record_step(["safe"])
        c.record_step(["safe", "active"])
        self.assertTrue(c.check_always("safe"))
        c.record_step(["unsafe"])
        self.assertFalse(c.check_always("safe"))

    def test_eventually_property(self):
        c = TemporalLogicTrajectoryChecker()
        c.record_step(["init"])
        c.record_step(["work"])
        self.assertFalse(c.check_eventually("done"))
        c.record_step(["done"])
        self.assertTrue(c.check_eventually("done"))
