# Remove Duplicates from Sorted List II

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_nodes(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

def node_list(arr):
    head = ListNode(arr[0])
    cur = head
    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head


class Solution(object):
    def deleteDuplicates(self, head):
        
        dummy = ListNode(0)
        tail = dummy
        while head:
            if head.next and head.val == head.next.val:
                val = head.val

                while head and head.val == val:
                    head = head.next
            else:
                tail.next = head
                tail = tail.next
                head = head.next
        tail.next = None
        return dummy.next


s = Solution()
print(list_nodes(s.deleteDuplicates(node_list([1, 2, 3, 3, 4, 4, 5])))) # [1, 2, 5]
print(list_nodes(s.deleteDuplicates(node_list([1, 1, 1, 2, 3]))))       # [2, 3]
print(list_nodes(s.deleteDuplicates(node_list([1, 2, 2]))))             # [1]
print(list_nodes(s.deleteDuplicates(node_list([1, 1, 1]))))             # []