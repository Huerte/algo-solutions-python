def reverse_ascending(items):
    result = []

    for i in range(len(items) - 1):
        temp = []
        for j in range(i):
            print(f'{j} -> {items[j]}  >  {i} -> {items[i]}')
            if items[j] > items[i]:
                break
            temp.append(items[j])

        for it in temp:
            result.append(it)

    return result

arr = [1, 2, 3, 4, 5]
print(reverse_ascending(arr))