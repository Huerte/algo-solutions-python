# Problem: Daily Temperatures
# Source: https://leetcode.com/problems/daily-temperatures/
# Note: Stack implementation mistakenly uses an if-statement instead of a while-loop, resolving at most one pending day.
# Status: In Progress (Logic Error)


class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = []

        for i in range(n):
            if stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index

            stack.append(i)

        return answer


if __name__ == "__main__":
    solution = Solution()
    result = solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    print("Result:", result)
    assert result == [1, 1, 4, 2, 1, 1, 0, 0], f"Expected [1, 1, 4, 2, 1, 1, 0, 0], got {result}"
