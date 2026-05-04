# Geeksforgeeks - Peak element

class Solution:   
    def peakElement(self, arr):
        if len(arr) == 1:
            return 0
            
        for i in range(len(arr)):
            if i == 0:
                if float('-inf') < arr[i] and arr[i] > arr[i + 1]:
                    return i
            elif i == len(arr) - 1:
                if arr[i-1] < arr[i] and arr[i] > float('-inf'):
                    return i
            else:
                if arr[i-1] < arr[i] and i + 1 < len(arr) and arr[i] > arr[i+1]:
                    return i
        return False
    
s = Solution()
print(s.peakElement([1, 2, 4, 5, 7, 8, 3])) # True
print(s.peakElement([1, 2, 3, 4, 5]))       # True
print(s.peakElement([1, 2]))                # True
print(s.peakElement([-1]))                  # True