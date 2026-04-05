# Count Good Triplets

class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        n = len(arr)
        count = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count

s = Solution()
print(s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3)) # 4
print(s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1)) # 0