# Palindrome Check (Ignoring Non-Alphanumeric)

def palindrome(s):
    new_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
    return new_s == new_s[::-1]

print(palindrome("A man, a plan, a canal: Panama"))