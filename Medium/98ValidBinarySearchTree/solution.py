from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper Function
        def validChecker(node, left, right):
            # If there is no node, then it's just true
            if not node:
                return True
            # if the value does not fall into the boundaray, (left and right),
            # then it's false!
            if not (node.val > left and node.val < right):
                return False
            # Both needs to be true to be a valid binary tree.
            return validChecker(node.left, left, node.val) and validChecker(
                node.right, node.val, right
            )

        return validChecker(root, float("-inf"), float("inf"))
