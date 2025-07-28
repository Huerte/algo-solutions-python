class Solution(object):
    def mySqrt(self, x):
        difference = 1
        initial_guess = x / 2
        prev_result = 0

        while difference > 0.1:
            initial_guess = (initial_guess + (x / initial_guess)) / 2
            difference = abs(prev_result - initial_guess)
            prev_result = initial_guess

        return initial_guess

sol = Solution()
print(sol.mySqrt(16))