from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root]
        while q:
            n = len(q)
            count = 0
            sum_ = 0
            for i in range(n):
                node = q.pop(0)
                count += 1
                sum_ += node.val
                if node.left:
                        q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum_ / count)
        return res

# Time Complexity: O(N)
# Space Complexity: O(N)