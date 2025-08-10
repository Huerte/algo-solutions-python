# 📜 Problem — Cable Connection Optimization
# Description:
# Given n coordinates (x, y), find the minimum total cable length needed to connect all points.
# The cable runs horizontally to cover the x-range and vertically to reach the median y-coordinate.
# This appears to be a custom optimization problem.
#
# Input:
# - An integer `n` representing the number of coordinates
# - n lines of space-separated integers representing (x, y) coordinates
#
# Output:
# - An integer representing the minimum total cable length
#
# Status: 🔄 IN PROGRESS - Needs clarification

def calculate_cable_length(coordinates):
    if not coordinates:
        return 0
    
    coord_x = [coord[0] for coord in coordinates]
    coord_y = [coord[1] for coord in coordinates]
    
    # Horizontal cable length (x-range)
    cable_destination = max(coord_x) - min(coord_x)
    
    # Vertical cable length (to median y-coordinate)
    coord_y.sort()
    if len(coord_y) % 2 == 0:
        median = (coord_y[(len(coord_y) // 2) - 1] + coord_y[(len(coord_y) // 2)]) // 2
    else:
        median = coord_y[len(coord_y) // 2]
    
    return cable_destination + median

# Test cases with assertions
# Example 1
coordinates1 = [(0, 0), (1, 1), (2, 2)]
assert calculate_cable_length(coordinates1) == 2

# Example 2
coordinates2 = [(0, 0), (5, 0), (10, 0)]
assert calculate_cable_length(coordinates2) == 10

# Example 3
coordinates3 = [(1, 1), (2, 2), (3, 3), (4, 4)]
assert calculate_cable_length(coordinates3) == 3

# Example 4
coordinates4 = [(0, 0)]
assert calculate_cable_length(coordinates4) == 0

print("All test cases passed!")
