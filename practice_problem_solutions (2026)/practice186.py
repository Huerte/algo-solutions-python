# CodeWars - Meeting

def meeting(s):
    names = []
    for name in s.split(';'):
        first, last = name.upper().split(':')
        names.append([last, first])
    
    return ''.join(f"({last}, {name})" for last, name in sorted(names, key=lambda x: (x[0], x[1])))