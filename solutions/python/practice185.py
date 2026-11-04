# Range Sum of BST

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
