# CodeWars - The Supermarket Queue

def queue_time(customers, n):
    
    queus = [0] * n
    
    for t in customers:
        i = queus.index(min(queus))
        queus[i] += t
    
    return max(queus)

print(queue_time([5,3,4], 1)) # 12
print(queue_time([10,2,3,3], 2)) # 10
print(queue_time([2,3,10], 2)) # 12