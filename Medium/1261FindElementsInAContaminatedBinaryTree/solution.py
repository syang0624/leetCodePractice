from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hash = set()
        root.val = 0
        self.hash.add(root.val)
        def dfs(node):
            if node.left:
                node.left.val = node.val * 2 + 1
                self.hash.add(node.left.val)
                dfs(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                self.hash.add(node.right.val)
                dfs(node.right)
        dfs(root)


    def find(self, target: int) -> bool:
        if target in self.hash:
            return True
        else:
            return False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

# Time Complexity: O(N)
# Space Complexity: O(N)