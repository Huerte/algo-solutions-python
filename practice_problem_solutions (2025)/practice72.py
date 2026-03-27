# 📜 Problem — Valid Parentheses
# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the
# input string is valid. An input string is valid if open brackets are closed by the same type of
# brackets and in the correct order.
# 
# Example:
# - Input: "()" → Output: true
# - Input: "()[]{}" → Output: true
# - Input: "(]" → Output: false
# - Input: "([)]" → Output: false
# 
# Status: 🔄 IN PROGRESS - Needs fixing

def is_valid_parentheses(s):
    if not s:
        return True
    
    # Map closing brackets to their corresponding opening brackets
    brackets_map = {
        '}': '{', 
        ')': '(', 
        ']': '['
    }
    
    stack = []
    
    for char in s:
        if char in brackets_map:
            # Closing bracket
            if not stack or stack.pop() != brackets_map[char]:
                return False
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

# Test cases with assertions
assert is_valid_parentheses("()") == True
assert is_valid_parentheses("()[]{}") == True
assert is_valid_parentheses("(]") == False
assert is_valid_parentheses("([)]") == False
assert is_valid_parentheses("{[]}") == True
assert is_valid_parentheses("") == True
assert is_valid_parentheses("(") == False
assert is_valid_parentheses(")") == False

print("All test cases passed!")