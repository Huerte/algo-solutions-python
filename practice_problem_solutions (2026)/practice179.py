# GeeksForGeeks - Indexes of Subarray Sum

arr = [1, 2, 3, 7, 5]
def subarraySum(arr, target):
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                x = sum(arr[i:j+1])
                if x == target:
                    return [i+1, j+1]
                elif x > target:
                    break
        return [-1]

print(subarraySum(arr, 12))