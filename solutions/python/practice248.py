# CodeWars - Return the Missing Element
# Problem: Return the Missing Element
# Source: https://www.codewars.com/kata/5299413901337c637e000004
# Note: Finds the missing digit from a sequence containing digits 0 through 9 using sorting or the difference between the expected and actual sums.
# My solution
def get_missing_element(seq): 
    for num, i in zip(sorted(seq), range(len(seq))):
        if num != i:
            return i
    return 9

# Other clever solution
def get_missing_element(seq): 
    return 45 - sum(seq)

print(get_missing_element([0,5,1,3,2,9,7,6,4])) # 8
print(get_missing_element([9,2,4,5,7,0,8,6,1])) # 3
print(get_missing_element([9,2,4,5,3,0,8,6,1])) # 7
