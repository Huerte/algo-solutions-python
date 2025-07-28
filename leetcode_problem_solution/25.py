#Average without min and max element then print in two decimal format

n = int(input("Enter number of  integers (N): "))
print(f"Enter {n} integers")
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.remove(min(arr))
arr.remove(max(arr))

average = sum(arr) / (n - 2)
print(f"Average: {average: .2f}")