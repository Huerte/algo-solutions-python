# Valid Parentheses

def valid_parenthesis(s):

    valid = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    temp = []

    for c in s:
        if temp and c in valid and valid[c] in temp:
            temp.pop()
        else:
            temp.append(c)
    
    return not temp


print(valid_parenthesis('{[()]}'))
print(valid_parenthesis('({)}'))
print(valid_parenthesis('{([])}][]'))