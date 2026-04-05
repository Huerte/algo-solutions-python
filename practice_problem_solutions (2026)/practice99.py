# Minimum Bit Flips to Convert Number

class Solution(object):
    def minBitFlips(self, start, goal):
        start_b = format(start, 'b')
        goal_b = format(goal, 'b')

        max_len = len(max([start_b, goal_b], key=len))

        start_b = start_b.zfill(max_len)
        goal_b = goal_b.zfill(max_len)

        print(start_b, goal_b)

        i = 0
        flip_count = 0
        while i < max_len:
            if start_b[i] != goal_b[i]:
                flip_count += 1
            i += 1
        return flip_count
    
s = Solution()
print(s.minBitFlips(10, 7)) # 3
print(s.minBitFlips(3, 4)) # 3