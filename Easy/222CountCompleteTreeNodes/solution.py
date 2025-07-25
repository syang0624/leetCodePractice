from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
       
        return 0

# Time Complexity: O(N)
# Space Complexity: O(H)