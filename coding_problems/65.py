# 📜 Problem — Valid Number
# Description:
# A valid number can be split up into these components (in order):
# 1. A decimal number or an integer.
# 2. (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):
# 1. (Optional) A sign character (either '+' or '-').
# 2. One of the following formats:
#    a. One or more digits, followed by a dot '.', followed by one or more digits.
#    b. One or more digits, followed by a dot '.'.
#    c. A dot '.', followed by one or more digits.
#    d. One or more digits.
# An integer can be split up into these components (in order):
# 1. (Optional) A sign character (either '+' or '-').
# 2. One or more digits.
#
# Input:
# - s: A string to validate
# - 1 <= s.length <= 20
# - s consists of only English letters, digits (0-9), plus '+', minus '-', or dot '.'
#
# Output:
# - A boolean indicating whether the string is a valid number
#
# Status: ✅ SOLVED

def isNumber(s):
    # Remove leading and trailing whitespace
    s = s.strip()
    
    if not s:
        return False
    
    # Check for 'e' or 'E' (scientific notation)
    if 'e' in s.lower():
        parts = s.lower().split('e')
        if len(parts) != 2:
            return False
        return isDecimal(parts[0]) and isInteger(parts[1])
    
    return isDecimal(s)

def isDecimal(s):
    if not s:
        return False
    
    # Handle sign
    if s[0] in '+-':
        s = s[1:]
    
    if not s:
        return False
    
    # Check if it's just digits
    if s.isdigit():
        return True
    
    # Check if it contains a dot
    if '.' in s:
        parts = s.split('.')
        if len(parts) != 2:
            return False
        
        # At least one part must contain digits
        if not parts[0] and not parts[1]:
            return False
        
        # Check parts
        if parts[0] and not parts[0].isdigit():
            return False
        if parts[1] and not parts[1].isdigit():
            return False
        
        return True
    
    return False

def isInteger(s):
    if not s:
        return False
    
    # Handle sign
    if s[0] in '+-':
        s = s[1:]
    
    return s.isdigit()

# Test cases with assertions
# Valid numbers
assert isNumber("2") == True
assert isNumber("0089") == True
assert isNumber("-0.1") == True
assert isNumber("+3.14") == True
assert isNumber("4.") == True
assert isNumber("-.9") == True
assert isNumber("2e10") == True
assert isNumber("-90E3") == True
assert isNumber("3e+7") == True
assert isNumber("+6e-1") == True
assert isNumber("53.5e93") == True

# Invalid numbers
assert isNumber("abc") == False
assert isNumber("1a") == False
assert isNumber("1e") == False
assert isNumber("e3") == False
assert isNumber("99e2.5") == False
assert isNumber("--6") == False
assert isNumber("-+3") == False
assert isNumber("95a54e53") == False

print("All test cases passed!")
