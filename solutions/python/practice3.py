# Problem: Cable Connection Optimization
# Source: 
# Note: Calculates minimum cable length along x-axis to span all coordinates
#
# Description:
# Given n coordinates (x, y), find the minimum total cable length needed to connect all points.
# The cable runs horizontally to cover the x-range.
#
# Input:
# - An integer `n` representing the number of coordinates
# - n lines of space-separated integers representing (x, y) coordinates
#
# Output:
# - An integer representing the minimum total cable length
#
# Status: ✅ SOLVED

def calculate_cable_length(coordinates):
    if not coordinates:
        return 0
    
    coord_x = [coord[0] for coord in coordinates]
    
    # Horizontal cable length (x-range)
    cable_destination = max(coord_x) - min(coord_x)
    return cable_destination

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
