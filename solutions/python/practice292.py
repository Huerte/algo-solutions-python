# HackerRank - The Hurdle Race
# Problem: The Hurdle Race
# Source: https://www.hackerrank.com/challenges/the-hurdle-race/problem
# Note: Calculates the minimum number of potion doses needed to clear the tallest hurdle.
def hurdleRace(k, height):
    return max(height) - k if k < max(height) else 0

print(hurdleRace(7, [1,6,3,5,2])) # 0
print(hurdleRace(4, [1,6,3,5,2])) # 2
print(hurdleRace(2, [3,5,7,9,1])) # 7
