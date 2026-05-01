# Geeksforgeeks - Kth Largest in a Stream

import heapq
class Solution:
    def kthLargest(self, arr, k):
        heap = []
        res = []
        
        for num in arr:
            heapq.heappush(heap, num)
            
            if len(heap) > k:
                heapq.heappop(heap)
            
            if len(heap) < k:
                res.append(-1)
            else:
                res.append(heap[0])
        
        return res

s = Solution()
print(s.kthLargest([1, 2, 3, 4, 5], 2)) # [-1, 1, 2, 3, 4]
print(s.kthLargest([1, 2, 3, 4, 5], 3)) # [-1, -1, 1, 2, 3]
print(s.kthLargest([1, 2, 3, 4, 5], 4)) # [-1, -1, -1, 1, 2]