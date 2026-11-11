# CodeWars - Meeting
# Problem: Meeting
# Source: https://www.codewars.com/kata/59df2f8f08c6cec835000012
# Note: Converts names to uppercase, sorts guests alphabetically by last name and then first name, and formats each name as (LAST, FIRST).
def meeting(s):
    names = []
    for name in s.split(';'):
        first, last = name.upper().split(':')
        names.append([last, first])
    
    return ''.join(f"({last}, {name})" for last, name in sorted(names, key=lambda x: (x[0], x[1])))
