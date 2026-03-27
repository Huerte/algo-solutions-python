# Remove Duplicates from Sorted Array

def remove_duplicates(arr):
    return len(set(arr))

print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))