# 📜 Problem — Longest Substring Without Repeating Characters
# Description:
# Given a string, find the length of the longest substring without repeating characters.
# 
# Example:
# - Input: "abcabcbb" → Output: 3 (substring "abc" has length 3)
# - Input: "bbbbb" → Output: 1 (substring "b" has length 1)
# - Input: "pwwkew" → Output: 3 (substring "wke" has length 3)
# 
# Status: 🔄 IN PROGRESS - Needs fixing

def longest_substring_without_repeating(s):
    if not s:
        return 0
    
    max_length = 0
    for i in range(len(s)):
        seen = set()
        current_length = 0
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            current_length += 1
        max_length = max(max_length, current_length)
    
    return max_length

# Test cases with assertions
assert longest_substring_without_repeating("abcabcbb") == 3
assert longest_substring_without_repeating("bbbbb") == 1
assert longest_substring_without_repeating("pwwkew") == 3
assert longest_substring_without_repeating("") == 0
assert longest_substring_without_repeating("a") == 1
assert longest_substring_without_repeating("au") == 2
assert longest_substring_without_repeating("dvdf") == 3

print("All test cases passed!")