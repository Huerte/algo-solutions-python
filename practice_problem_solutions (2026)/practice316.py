# CodeWars - Return pyramids

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