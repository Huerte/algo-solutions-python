# Mirror Distance of an Integer

class Solution(object):
    def mirrorDistance(self, n):
        return abs(n - int(str(n)[::-1]))