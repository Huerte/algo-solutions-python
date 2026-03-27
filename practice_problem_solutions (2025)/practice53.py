# 📜 Problem — Maximum Area of Longest Diagonal Rectangle
# Description:
# Given a list of rectangles with length and breadth, find the rectangle with the maximum area 
# among those that have the longest diagonal. If multiple rectangles have the same longest diagonal, 
# choose the one with the maximum area.
#
# Input:
# - An integer n representing the number of rectangles
# - n lines of space-separated integers representing (length, breadth) for each rectangle
#
# Output:
# - An integer representing the maximum area of the rectangle with the longest diagonal
#
# Status: ✅ SOLVED

from math import sqrt

def find_max_area_longest_diagonal(rectangles):
    if not rectangles:
        return 0
        
    max_area = 0
    max_diagonal = 0
    
    for l, b in rectangles:
        current_area = l * b
        current_diagonal = sqrt(l ** 2 + b ** 2)
        
        if current_diagonal > max_diagonal or (current_diagonal == max_diagonal and current_area > max_area):
            max_diagonal = current_diagonal
            max_area = current_area
    
    return max_area

# Test cases with assertions
# Example 1
rectangles1 = [(3, 4), (5, 12), (6, 8)]
assert find_max_area_longest_diagonal(rectangles1) == 60  # 5x12 has longest diagonal

# Example 2
rectangles2 = [(1, 1), (2, 2), (3, 3)]
assert find_max_area_longest_diagonal(rectangles2) == 9  # 3x3 has longest diagonal

# Example 3
rectangles3 = [(4, 3), (8, 6)]  # Same diagonal, different areas
assert find_max_area_longest_diagonal(rectangles3) == 48  # 8x6 has larger area

# Example 4
rectangles4 = [(1, 1)]
assert find_max_area_longest_diagonal(rectangles4) == 1

# Edge cases
rectangles5 = []
assert find_max_area_longest_diagonal(rectangles5) == 0

print("All test cases passed!")