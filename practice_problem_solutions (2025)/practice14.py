# 📜 Problem — Rotate List
# Description:
# Given the head of a linked list, rotate the list to the right by k places.
# A rotation involves moving the last k nodes to the front of the list.
#
# Input:
# - head: The head of a linked list
# - k: A non-negative integer representing the number of rotations
# - 0 <= k <= 2 * 10^9
#
# Output:
# - The head of the rotated linked list
#
# Status: ✅ SOLVED

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    
    # Count the length of the list
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1
    
    # Make the list circular
    current.next = head
    
    # Calculate effective rotation
    k = k % length
    
    # Find the new tail
    for _ in range(length - k - 1):
        head = head.next
    
    # Break the circular list
    new_head = head.next
    head.next = None
    
    return new_head

# Helper function to create linked list from array
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to array
def linkedListToArray(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases with assertions
# Example 1
head1 = createLinkedList([1,2,3,4,5])
result1 = rotateRight(head1, 2)
assert linkedListToArray(result1) == [4,5,1,2,3]

# Example 2
head2 = createLinkedList([0,1,2])
result2 = rotateRight(head2, 4)
assert linkedListToArray(result2) == [2,0,1]

# Edge cases
head3 = createLinkedList([1, 2])
result3 = rotateRight(head3, 1)
assert linkedListToArray(result3) == [2, 1]

head4 = createLinkedList([1])
result4 = rotateRight(head4, 0)
assert linkedListToArray(result4) == [1]

print("All test cases passed!")