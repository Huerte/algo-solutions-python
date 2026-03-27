# 📜 Problem — Backspace String Compare
# Description:
# Given two strings s and t, return true if they are equal when both are typed into 
# empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.
#
# Input:
# - Two strings `s` and `t` containing lowercase letters and '#' characters
#
# Output:
# - A boolean indicating whether the strings are equal after processing backspaces
#
# Status: ✅ SOLVED

def backspaceStringCompare(s, t):
    def processString(string):
        result = []
        for char in string:
            if char != "#":
                result.append(char)
            elif result:
                result.pop()
        return result
    
    s_processed = processString(s)
    t_processed = processString(t)
    
    return s_processed == t_processed

# Test cases with assertions
# Example 1
s1, t1 = "ab#c", "ad#c"
assert backspaceStringCompare(s1, t1) == True

# Example 2
s2, t2 = "ab##", "c#d#"
assert backspaceStringCompare(s2, t2) == True

# Example 3
s3, t3 = "a#c", "b"
assert backspaceStringCompare(s3, t3) == False

# Example 4
s4, t4 = "y#fo##f", "y#f#o##f"
assert backspaceStringCompare(s4, t4) == True

# Example 5
s5, t5 = "a##c", "#a#c"
assert backspaceStringCompare(s5, t5) == True

# Edge cases
s6, t6 = "", ""
assert backspaceStringCompare(s6, t6) == True

s7, t7 = "###", "###"
assert backspaceStringCompare(s7, t7) == True

print("All test cases passed!")