# Backspaces in string

def clean_string(s):
    seen = []
    
    for c in s:
        if seen and c == '#':
            seen.pop()
        elif c != '#':
            seen.append(c)
    
    return ''.join(seen)