# Valid Braces
# Problem: Valid Braces
# Source: https://www.codewars.com/kata/5277c8a221e209d3f6000b56
# Note: Validates the order and matching of parentheses, square brackets, and curly braces using stack and string-replacement approaches.
def valid_braces(string):
    brace = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    
    seen = []
    
    for c in string:
        if seen and c in brace and brace[c] == seen[-1]:
            seen.pop()
            continue
        seen.append(c)
    return not seen

# Clever Solution From CodeWars
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''

print(valid_braces('()'))      # True
print(valid_braces('(){}[]'))  # True
print(valid_braces('([{}])'))  # True
print(valid_braces('(}'))      # False
print(valid_braces('[(])'))    # False
