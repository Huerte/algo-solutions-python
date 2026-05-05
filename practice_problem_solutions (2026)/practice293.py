# Rotate List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodes_to_list(head):
    arr = []
    temp = head
    while temp:
        arr.append(temp.val)
        temp = temp.next
    return arr

def list_to_nodes(arr):
    new = ListNode(0)
    temp = new
    for num in arr:
        temp.next = ListNode(num)
        temp = temp.next
    return new.next

class Solution(object):
    def rotateRight(self, head, k):
        
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        d = k % len(arr)
        arr = arr[-d:] + arr[:-d]

        new = ListNode(0)
        temp = new
        for num in arr:
            temp.next = ListNode(num)
            temp = temp.next
        
        return new.next
    
s = Solution()
print(nodes_to_list(s.rotateRight(list_to_nodes([1,2,3,4,5]), 2)))   # [4,5,1,2,3]
print(nodes_to_list(s.rotateRight(list_to_nodes([0,1,2]), 4)))       # [2,0,1]