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