# Range Sum of BST
# Problem: Range Sum of BST
# Source: https://leetcode.com/problems/range-sum-of-bst/
# Note: Calculates the sum of all BST node values within the inclusive range [low, high] using BFS traversal.
from collections import deque
class Solution(object):
    def rangeSumBST(self, root, low, high):
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        return sum(num for num in res if num >= low and num <= high)
