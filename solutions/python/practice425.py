# Problem: Minimum Window Substring
# Source: https://leetcode.com/problems/minimum-window-substring/
# Topic: Sliding Window, Hash Map
# Status: IN PROGRESS

def min_window(s, t):
    if not s or not t:
        return ""

    need = {}
    for c in t:
        need[c] = need.get(c, 0) + 1

    window = {}
    formed = 0
    required = len(need)

    left = 0
    ans = (float("inf"), 0, 0)

    for right in range(len(s)):
        c = s[right]
        window[c] = window.get(c, 0) + 1

        if c in need and window[c] == need[c]:
            formed += 1

        while formed == required:
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            lc = s[left]
            window[lc] -= 1
            if lc in need and window[lc] == need[lc]:
                formed -= 1
            left += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

assert min_window("ADOBECODEBANC", "ABC") == "BANC"
assert min_window("a", "a") == "a"
assert min_window("a", "aa") == ""
