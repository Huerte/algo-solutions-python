# Valid Braces

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