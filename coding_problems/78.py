class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        head = ListNode()
        carry = (l1.val + l2.val) // 10

        current_node = head

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            total = v1 + v2 + carry
            carry = total // 10

            current_node.next = ListNode(total % 10)
            current_node = current_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next























def to_listnode(nums):
    dummy = ListNode(0)
    cur = dummy
    for n in nums:
        cur.next = ListNode(n)
        cur = cur.next
    return dummy.next

def to_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

s = Solution()

# Case 1: Basic short lists
l1 = to_listnode([2,4,3])
l2 = to_listnode([5,6,4])
print(to_list(s.addTwoNumbers(l1, l2)))
assert to_list(s.addTwoNumbers(l1, l2)) == [7,0,8]

# Case 2: Carry propagation
l1 = to_listnode([9,9,9])
l2 = to_listnode([1])
print(to_list(s.addTwoNumbers(l1, l2)))
assert to_list(s.addTwoNumbers(l1, l2)) == [0,0,0,1]

# Case 3: Different lengths
l1 = to_listnode([2,4])
l2 = to_listnode([5,6,4])
assert to_list(s.addTwoNumbers(l1, l2)) == [7,0,5]

# Case 4: Both single digits
l1 = to_listnode([0])
l2 = to_listnode([0])
assert to_list(s.addTwoNumbers(l1, l2)) == [0]

# Case 5: Long chain with no carry
l1 = to_listnode([1,1,1,1])
l2 = to_listnode([2,2,2,2])
assert to_list(s.addTwoNumbers(l1, l2)) == [3,3,3,3]

# Case 6: Long chain with full carry
l1 = to_listnode([9,9,9,9,9])
l2 = to_listnode([9,9,9,9,9])
assert to_list(s.addTwoNumbers(l1, l2)) == [8,9,9,9,9,1]

# Case 7: One empty list (treat as zero)
l1 = None
l2 = to_listnode([3,4,5])
assert to_list(s.addTwoNumbers(l1, l2)) == [3,4,5]

# Case 8: Large number + small number
l1 = to_listnode([1,8])
l2 = to_listnode([0])
assert to_list(s.addTwoNumbers(l1, l2)) == [1,8]

# Case 9: Zero + multi-digit
l1 = to_listnode([0])
l2 = to_listnode([7,3])
assert to_list(s.addTwoNumbers(l1, l2)) == [7,3]

# Case 10: Single carry at the end
l1 = to_listnode([5])
l2 = to_listnode([5])
assert to_list(s.addTwoNumbers(l1, l2)) == [0,1]

print("All tests passed.")
