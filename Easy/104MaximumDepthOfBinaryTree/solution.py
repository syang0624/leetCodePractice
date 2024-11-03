from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursion / DFS Solution
    # Time: O(N)
    # Space: O(H) where H is the height of the tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # Iterative / DFS Solution
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     stack = [[root, 1]]
    #     res = 1

    #     while stack:
    #         node, depth = stack.pop()

    #         if node:
    #             res = max(res, depth)
    #             stack.append([node.left, depth + 1])
    #             stack.append([node.right, depth + 1])
    #     return res

    # BFS Solution
    # Time: O(N)
    # Space: O(W) where W is the width of the tree
    # Time: O(N)
    # Space: O(H) where H is the height of the tree
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     level = 0
    #     queue = []
    #     queue.append(root)
    #     while queue:
    #         for i in range(len(queue)):
    #             s = queue.pop(0)
    #             if s.left:
    #                 queue.append(s.left)
    #             if s.right:
    #                 queue.append(s.right)
    #         level += 1
    #     return level
