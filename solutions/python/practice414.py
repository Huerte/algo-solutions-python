# Problem: Gas Station
# Source: https://leetcode.com/problems/gas-station/
# Note: Greedy tracking resets start index on deficit; a global gas/cost check rejects impossible circuits.
# Status: ✅ Done


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_stations = len(gas)
        current_tank = 0
        start_index = 0

        for i in range(total_stations):
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                start_index = i + 1
                current_tank = 0

        # A circuit exists only if total gas covers total cost; the greedy
        # scan above finds its start when that holds.
        if sum(gas) < sum(cost):
            return -1

        return start_index


if __name__ == "__main__":
    solution = Solution()
    assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    result = solution.canCompleteCircuit([2, 3, 4], [3, 4, 3])
    print("Result:", result)
    assert result == -1, f"Expected -1, got {result}"
