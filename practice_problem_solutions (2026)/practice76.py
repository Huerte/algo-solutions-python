# Insert Greatest Common Divisors in Linked List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        
        cur = head
        import math
        while cur and cur.next:
            temp = math.gcd(cur.val, cur.next.val)
            new_node = ListNode(temp, cur.next)
            cur.next = new_node
            cur = new_node.next
        
        return head


def to_linked_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next
    return head

s = Solution()
print(s.insertGreatestCommonDivisors(to_linked_list([18, 6, 10, 3])))