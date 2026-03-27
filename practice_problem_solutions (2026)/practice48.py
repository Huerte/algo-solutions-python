# Jump Game

def can_jump(arr):

    max_reach = 0

    for i in range(len(arr)):
        if i > max_reach:
            return False
        
        max_reach = max(arr[i] + i, max_reach)

        if max_reach >= len(arr) - 1:
            return True
    
    return False


print(can_jump([2, 1, 3, 1, 0, 1])) # == True
print(can_jump([3, 2, 1, 0, 4]))    # == False