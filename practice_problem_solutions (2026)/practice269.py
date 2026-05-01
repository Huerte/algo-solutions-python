# GeeksforGeeks - Longest Palindrome in a String

# My Sol;
class Solution:
    def longestPalindrome(self, s):
        palindrome = ""
        n = len(s)
        for i in range(n - 1):
            right = n
            while right > i:
                temp = s[i:right]
                if temp == temp[::-1] and len(temp) > len(palindrome):
                    palindrome = temp
                    break
                right -= 1
        return palindrome

# Optimized Sol;
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        res = ""
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            p1 = expand(i, i)
            if len(p1) > len(res):
                res = p1

            p2 = expand(i, i + 1)
            if len(p2) > len(res):
                res = p2
                
        return res

s = Solution()
print(s.longestPalindrome("bswrhxboawtdfqggqfdtwyypwnssnwpyyaobxhrwsb")) # wtdfqggqfdtw
print(s.longestPalindrome("aaaabbaa"))                                   # aabbaa
print(s.longestPalindrome("ababa"))                                      # ababa