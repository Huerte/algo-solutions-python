# HackerRank - Bigger is Greater

# Not my Sol;
def biggerIsGreater(w):
    arr = list(w)

    pivot = -1
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            pivot = i - 1
            break

    if pivot == -1:
        return 'no answer'

    for i in range(len(arr) - 1, pivot, -1):
        if arr[i] > arr[pivot]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            break

    arr[pivot + 1:] = sorted(arr[pivot + 1:])

    return ''.join(arr)


print(biggerIsGreater("ab"))  # "ba"
print(biggerIsGreater("bb"))  # "no answer"
print(biggerIsGreater("hefg"))  # "hegf"
print(biggerIsGreater("dkhc"))  # "hcdk"