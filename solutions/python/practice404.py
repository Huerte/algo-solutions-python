# CodeWars - Sum of Pairs
# Problem: Sum of Pairs
# Source: https://www.codewars.com/kata/54d81488b981293527000c8f
# Note: Finds the first pair of numbers, from left to right, that adds up to the target sum.
def sum_pairs(ints, s):
    
    seen = set()
    
    for num in ints:
        
        target = s - num
        
        if target in seen:
            return [target, num]
        
        seen.add(num)

print(sum_pairs([1, -2, 3, 0, -6, 1], -6)) # [0, -6]
print(sum_pairs([1, 4, 8, 7, 3, 15], 8))   # [1, 7]
print(sum_pairs([20, -13, 40], -7))        # None
