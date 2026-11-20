# Problem: Minimum Depth of Binary Tree
# Source: https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Topic: Tree, BFS

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_depth(root):
    if not root:
        return 0
    q = deque()
    q.append((root, 1))
    while q:
        node, depth = q.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return 0

def build(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root

assert min_depth(build([1])) == 1
assert min_depth(build([3, 9, 20, None, None, 15, 7])) == 2
assert min_depth(build([1, 2, None, 3, None, 4, None, 5])) == 5
assert min_depth(None) == 0
