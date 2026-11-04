# Longest Substring Without Repeating Characters
# Problem: Longest Substring Without Repeating Characters
# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Note: Attempts to find the longest substring without repeating characters by splitting the string whenever a duplicate character is encountered.
def substring(s):
    words = []
    cur = ""
    for c in s:
        if c.lower() in cur:
            words.append(cur)
            cur = ""
            continue
        cur += c
    if cur:
        words.append(cur)
    
    return max(words, key=len) if words else ""

print(substring("abcaba"))
print(substring(""))
