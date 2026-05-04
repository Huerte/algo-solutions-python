# Minimum Absolute Difference

class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()

        mn = float('inf')
        res = []

        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]

            if diff < mn:
                mn = diff
                res = [[arr[i], arr[i+1]]]
            elif diff == mn:
                res.append([arr[i], arr[i+1]])
        return res
    
s = Solution()
print(s.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])) # [[-14,-10],[19,23],[23,27]]
print(s.minimumAbsDifference([-25,-51,-29,-23,57,-18]))  # [[-25,-23]]
print(s.minimumAbsDifference([1,3,6,10,15]))             # [[1, 3]]