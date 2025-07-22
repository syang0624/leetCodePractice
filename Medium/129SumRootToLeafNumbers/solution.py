from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, count):
            if not root:
                return 0
            count = count * 10 + root.val
            if not root.left and not root.right:
                return count
            return dfs(root.left, count) + dfs(root.right, count)

        return dfs(root, 0)

# Time Complexity: O(N)
# Space Complexity: O(1)