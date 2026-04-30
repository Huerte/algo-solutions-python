# HackerRank - Jumping on the Clouds

def jumpingOnClouds(c):
    jumps = 0
    
    i = 0
    while i < len(c):
        
        if i + 2 < len(c) and c[i + 2] == 0:
            jumps += 1
            i += 2
            continue
        if i + 1 < len(c) and c[i + 1] == 0:
            jumps += 1
            i += 1
            continue
        
        jumps += 1
        i += 2
        
    return jumps - 1

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))  # 4
print(jumpingOnClouds([0, 0, 0, 1, 0, 0]))     # 3
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))     # 3