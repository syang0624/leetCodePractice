from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def dfs(node):
            if not node:
                return 0
            leftSum = max(0, dfs(node.left))
            rightSum = max(0, dfs(node.right))

            self.res = max(self.res, leftSum + rightSum + node.val)

            return max(leftSum, rightSum) + node.val

        dfs(root)
        return self.res
