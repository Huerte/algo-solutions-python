# CodeWars - Return pyramids
# Problem: Return pyramids
# Source: https://www.codewars.com/kata/5803a6d8db07c59fff00015f
# Note: Generates an ASCII pyramid with n floors and a trailing newline.
def pyramid(n):
    
    sp = n - 1
    mid = 0
    
    res = []
    
    for _ in range(n - 1):
        
        res.append(' ' * sp + '/' + ' ' * mid + '\\')
        
        sp -= 1
        mid += 2
    
    res.append('/' + '_' * mid + '\\')
    
    return '\n'.join(res) + '\n'

print(pyramid(1)) # '/\\\n'
print(pyramid(2)) # ' /\\\n/__\\\n'
print(pyramid(3)) # '  /\\\n /  \\\n/____\\\n'
