from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]
        maxSum = float("-inf")
        maxLevel = 1
        currentLevel = 1
        while queue:
            currentSum = 0

            for _ in range(len(queue)):
                node = queue.pop(0)
                currentSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if currentSum > maxSum:
                maxSum = currentSum
                maxLevel = currentLevel
            currentLevel += 1
        return maxLevel


# Time: O(N)
# Space: O(W)
