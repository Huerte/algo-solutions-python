# Problem: Digit Frequency Score
# Source: https://leetcode.com/problems/digit-frequency-score/
# Note: Adding each digit once per occurrence is equivalent to weighting it by frequency.
# Status: ✅ Done


class Solution(object):
    def digitFrequencyScore(self, n):
        """Return the sum of the decimal digits of n."""
        return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    solution = Solution()
    assert solution.digitFrequencyScore(122) == 5
    assert solution.digitFrequencyScore(101) == 2
    assert solution.digitFrequencyScore(9999) == 36
