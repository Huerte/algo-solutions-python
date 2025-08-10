# 📜 Problem — Longest Common Prefix
# Description:
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Input:
# - An array of strings `strs` where 1 <= strs.length <= 200
# - Each string in strs consists of only lowercase English letters
# - 0 <= strs[i].length <= 200
#
# Output:
# - A string representing the longest common prefix
#
# Status: ✅ SOLVED

def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    sample_word = strs[0]

    for word in strs[1:]:
        while sample_word and word[:len(sample_word)] != sample_word:
            sample_word = sample_word[:-1]
    return sample_word

# Test cases with assertions
# Example 1
assert longestCommonPrefix(["flower","flow","flight"]) == "fl"

# Example 2
assert longestCommonPrefix(["ab", "a"]) == "a"

# Example 3
assert longestCommonPrefix(["dog","racecar","car"]) == ""

# Example 4
assert longestCommonPrefix(["interspecies","interstellar","interstate"]) == "inters"

# Example 5
assert longestCommonPrefix(["throne","throne"]) == "throne"

# Edge cases
assert longestCommonPrefix([""]) == ""
assert longestCommonPrefix(["a"]) == "a"
assert longestCommonPrefix(["", "b"]) == ""

print("All test cases passed!")