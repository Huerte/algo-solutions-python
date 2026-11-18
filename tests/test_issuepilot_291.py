import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "solutions", "python"))
from practice413 import Solution  # noqa: E402


class DailyTemperaturesTests(unittest.TestCase):
    def test_one_warmer_day_resolves_two_pending_days(self):
        self.assertEqual(Solution().dailyTemperatures([70, 60, 75]), [2, 1, 0])


if __name__ == "__main__":
    unittest.main()
