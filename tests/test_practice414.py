"""Regression tests for the Gas Station solution (issue #292)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solutions", "python"))
from practice414 import Solution  # noqa: E402


class GasStationTests(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_known_valid_circuit(self):
        self.assertEqual(
            self.solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3
        )

    def test_no_circuit_when_total_gas_below_total_cost(self):
        self.assertEqual(self.solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]), -1)

    def test_no_circuit_with_single_station(self):
        self.assertEqual(self.solution.canCompleteCircuit([1], [2]), -1)

    def test_total_zero_still_has_a_circuit(self):
        self.assertEqual(self.solution.canCompleteCircuit([2, 1], [1, 2]), 0)
        self.assertEqual(self.solution.canCompleteCircuit([3, 7], [5, 5]), 1)

    def test_every_station_valid(self):
        self.assertEqual(self.solution.canCompleteCircuit([1, 1, 1, 1], [1, 1, 1, 1]), 0)


if __name__ == "__main__":
    unittest.main()
