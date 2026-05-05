# CodeWars - +1 Array

def up_array(arr):
    if not arr or any([c < 0 or c > 9 for c in arr]):
        return None
    
    carry = 1
    
    for i in range(len(arr) - 1, -1, -1):
        if carry < 1:
            break

        temp = arr[i] + carry
        if temp > 9:
            arr[i] = temp % 10
        else:
            arr[i] = temp

        carry = temp // 10
    
    if carry > 0:
        arr.insert(0, carry)
    
    return arr

print(up_array([4, 3, 2, 5])) # [4, 3, 2, 6]
print(up_array([9, 9, 9]))    # [1, 0, 0, 0]
print(up_array([1, 2, 3]))    # [1, 2, 4]
print(up_array([1, -9]))      # None
print(up_array([1, 10]))      # None