# Problem: Merge k Sorted Lists
# Source: https://leetcode.com/problems/merge-k-sorted-lists/
# Topic: Linked List, Heap

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode()
    cur = dummy
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = cur.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def make_list(vals):
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

assert to_list(mergeKLists([make_list([1,4,5]), make_list([1,3,4]), make_list([2,6])])) == [1,1,2,3,4,4,5,6]
assert to_list(mergeKLists([])) == []
assert to_list(mergeKLists([make_list([])])) == []
assert to_list(mergeKLists([make_list([1,2]), make_list([3,4])])) == [1,2,3,4]
