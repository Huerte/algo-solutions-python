class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr
def to_listnode(nums):
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None
        
        new_head = ListNode()
        tail = new_head

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        seen = []
        for num in arr:
            if not seen:
                tail.next = ListNode(val=num)
                tail = tail.next
            elif seen and num not in seen:
                tail.next = ListNode(val=num)
                tail = tail.next
            seen.append(num)

        return new_head.next
    


s = Solution()
l1 = to_listnode([1,1,2,3,3])

print(to_list(s.deleteDuplicates(l1)))