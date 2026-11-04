# Backspaces in string
# Problem: Backspaces in string
# Source: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3
# Note: Uses a stack to process the string, removing the previous character whenever a '#' backspace character is encountered.
def clean_string(s):
    seen = []
    
    for c in s:
        if seen and c == '#':
            seen.pop()
        elif c != '#':
            seen.append(c)
    
    return ''.join(seen)
