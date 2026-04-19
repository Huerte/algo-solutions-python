# HackerRank - Picking Numbers

def pickingNumbers(a):
    subs = []
    i = 0

    a.sort()

    while i < len(a) - 1:
        temp = [a[i]]
        
        for j in range(i + 1, len(a)):
            add = True
            for num in temp:
                if abs(num - a[j]) > 1:
                    add = False
            if add:
                temp.append(a[j])

        subs.append(temp)

        i += 1
                
    return len(max(subs, key=len))

print(pickingNumbers([1,1,2,2,4,4,5,5,5])) # 5
print(pickingNumbers([4,6,5,3,3,1]))       # 3
print(pickingNumbers([1,2,2,3,1,2]))       # 5