# 📜 Problem — String Jump Decoder
# Description:
# Given a string where even-indexed characters are letters and odd-indexed characters are digits,
# decode the string by taking characters at even indices and jumping forward by the digit at the
# next odd index to get the next character.
# 
# Example:
# - Input: "a1b2c3" → Output: "a" + jump('a', 1) + jump('b', 2) + jump('c', 3)
# - For "a1b2c3": a + (a+1) + (b+2) + (c+3) = "abc"
# 
# Status: 🔄 IN PROGRESS - Needs clarification

def string_jump_decoder(s):
    if not s or len(s) < 2:
        return s
    
    result = []
    i = 0
    while i < len(s):
        if i % 2 == 0:  # Even index - letter
            if i < len(s):
                result.append(s[i])
        else:  # Odd index - digit
            if i < len(s) and i > 0:
                try:
                    jump = int(s[i])
                    prev_char = s[i-1]
                    # Jump forward by the digit value
                    new_char = chr(ord(prev_char) + jump)
                    result.append(new_char)
                except (ValueError, OverflowError):
                    # If jump is too large or invalid, skip
                    pass
        i += 1
    
    return "".join(result)

# Test cases with assertions
assert string_jump_decoder("a1b2c3") == "abc"  # a + (a+1) + (b+2) + (c+3)
assert string_jump_decoder("x2") == "x"  # Only one letter
assert string_jump_decoder("a1") == "a"  # Letter + digit
assert string_jump_decoder("") == ""
assert string_jump_decoder("a") == "a"  # Single letter

print("All test cases passed!")