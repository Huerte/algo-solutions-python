import math

def viralAdvertising(n):
    shared = 5
    likes = 0

    for _ in range(n):
        like = shared // 2
        likes += like
        shared = like * 3
    
    return likes

print(viralAdvertising(3)) # 9
print(viralAdvertising(4)) # 15