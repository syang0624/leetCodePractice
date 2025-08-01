from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float("inf")
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nonlocal prev, res
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)
        
        dfs(root)
        return res

# Time Complexity:O(N)
# Space Complexity:O(H)
