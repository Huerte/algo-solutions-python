n = int(input())
a = []
for i in range(n):
    a.append(input())
c = input()
print("\n".join([x for x in a if c in x]))