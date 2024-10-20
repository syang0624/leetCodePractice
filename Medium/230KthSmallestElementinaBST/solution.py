from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         self.lst = []
#         def dfs(node):
#             if not node:
#                 return
#             self.lst.append(node.val)
#             dfs(node.left)
#             dfs(node.right)


#         dfs(root)
#         self.lst.sort()
#         return self.lst[k-1]
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            n += 1
            if n == k:
                return node.val
            node = node.right
