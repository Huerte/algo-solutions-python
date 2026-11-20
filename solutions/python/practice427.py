# Problem: Serialize and Deserialize Binary Tree
# Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Topic: Tree, BFS, String
# Status: IN PROGRESS

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        # BFS level-order serialization
        if not root:
            return "null"
        result = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        return ",".join(result)

    def deserialize(self, data):
        # TODO: implement BFS deserialization
        pass
