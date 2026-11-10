# Problem: String Jump Decoder
# Source: 
# Note: Decodes string by extracting characters at even indices
# 
# Description:
# Given a string where even-indexed characters are letters and odd-indexed characters are digits,
# decode the string by taking characters at even indices.
# 
# Status: ✅ SOLVED

def string_jump_decoder(s):
    if not s:
        return ""
    return s[::2]

# Test cases with assertions
assert string_jump_decoder("a1b2c3") == "abc"  # a + (a+1) + (b+2) + (c+3)
assert string_jump_decoder("x2") == "x"  # Only one letter
assert string_jump_decoder("a1") == "a"  # Letter + digit
assert string_jump_decoder("") == ""
assert string_jump_decoder("a") == "a"  # Single letter

print("All test cases passed!")