fib = [0, 1]
n = int(input())
for i in range(n-2):
    fib.append(fib[i] + fib[i+1])

print(fib)