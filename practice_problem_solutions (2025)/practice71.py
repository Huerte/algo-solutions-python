# 📜 Problem — Most Frequent Even Number
# Description:
# Given a list of integers, find the most frequently occurring even number. If there are multiple
# even numbers with the same frequency, return the smallest one. If no even numbers exist, return None.
# 
# Example:
# - Input: [1, 2, 2, 3, 4, 4, 4, 5] → Output: 4 (appears 3 times)
# - Input: [1, 3, 5] → Output: None (no even numbers)
# 
# Status: ✅ SOLVED

def most_frequent_even(numbers):
    if not numbers:
        return None
    
    # Count frequencies of even numbers only
    even_counts = {}
    for num in numbers:
        if num % 2 == 0:
            even_counts[num] = even_counts.get(num, 0) + 1
    
    if not even_counts:
        return None
    
    # Find the most frequent even number, breaking ties by smaller value
    max_freq = max(even_counts.values())
    most_frequent = min(num for num, freq in even_counts.items() if freq == max_freq)
    
    return most_frequent

# Test cases with assertions
assert most_frequent_even([1, 2, 2, 3, 4, 4, 4, 5]) == 4
assert most_frequent_even([1, 3, 5]) == None
assert most_frequent_even([2, 2, 4, 4, 4, 6, 6]) == 4
assert most_frequent_even([2]) == 2
assert most_frequent_even([2, 4, 6, 8]) == 2  # All have frequency 1, return smallest
assert most_frequent_even([]) == None

print("All test cases passed!")