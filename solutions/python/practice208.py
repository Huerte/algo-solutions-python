# CodeWars - The Supermarket Queue
# Problem: The Supermarket Queue
# Source: https://www.codewars.com/kata/57b06f90e298a7b53d000a86
# Note: Calculates the total checkout time by assigning each customer to the till with the minimum accumulated time.
def queue_time(customers, n):
    
    queus = [0] * n
    
    for t in customers:
        i = queus.index(min(queus))
        queus[i] += t
    
    return max(queus)

print(queue_time([5,3,4], 1)) # 12
print(queue_time([10,2,3,3], 2)) # 10
print(queue_time([2,3,10], 2)) # 12
