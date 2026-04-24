# Furthest Point From Origin

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return abs(moves.count('R') - moves.count('L')) + moves.count('_')
    
s = Solution()
print(s.furthestDistanceFromOrigin("L_RL__R")) # 3
print(s.furthestDistanceFromOrigin("_R__LL_")) # 5
print(s.furthestDistanceFromOrigin("_______")) # 7