# 📜 Problem — Frequency Counter
# Description:
# Given a list of strings, count the frequency of each string and return a formatted result string
# showing each unique string and its count, sorted by frequency in descending order.
# 
# Example:
# - Input: ["a", "b", "a", "c", "b", "a"]
# - Output: "a - 3, b - 2, c - 1"
# 
# Status: 🔄 IN PROGRESS - Needs fixing

def frequency_counter(strings):
    if not strings:
        return ""
    
    # Count frequencies
    freq = {}
    for s in strings:
        freq[s] = freq.get(s, 0) + 1
    
    # Sort by frequency (descending) and then by string (ascending for ties)
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Format result
    result_parts = []
    for item, count in sorted_items:
        result_parts.append(f"{item} - {count}")
    
    return ", ".join(result_parts)

# Test cases with assertions
assert frequency_counter(["a", "b", "a", "c", "b", "a"]) == "a - 3, b - 2, c - 1"
assert frequency_counter(["hello", "world", "hello"]) == "hello - 2, world - 1"
assert frequency_counter([]) == ""
assert frequency_counter(["single"]) == "single - 1"
assert frequency_counter(["a", "a", "a"]) == "a - 3"

print("All test cases passed!")