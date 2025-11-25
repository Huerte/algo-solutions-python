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
    def mergeTwoLists(self, list1, list2):

        if not list1 or not list2:
            return None

        arr = []

        if list1:
            arr.append(list1.val)
            while list1.next:
                list1 = list1.next
                arr.append(list1.val)

        if list2:
            arr.append(list2.val)
            while list2.next:
                list2 = list2.next
                arr.append(list2.val)

        if len(arr) > 0:
            arr.sort()
            
            head = ListNode(val = arr[0])
            tail = head
            if len(arr) > 0:
                for num in arr[1:]:
                    tail.next = ListNode(val = num)
                    tail = tail.next
                    print(num, end=", ")

            print(to_list(head))

            return head
        
        return ListNode()
    




s = Solution()
l1 = to_listnode([])
l2 = to_listnode([])

print(to_list(s.mergeTwoLists(l1, l2)))