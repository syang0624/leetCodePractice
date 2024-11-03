from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, isLeft, depth):
            if not node:
                return depth
            if isLeft:
                depth = max(
                    depth, dfs(node.right, False, depth + 1), dfs(node.left, True, 0)
                )
            if not isLeft:
                depth = max(
                    depth, dfs(node.left, True, depth + 1), dfs(node.right, False, 0)
                )
            return depth

        return max(dfs(root.left, True, 0), dfs(root.right, False, 0))
