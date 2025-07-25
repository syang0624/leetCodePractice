from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = 0
        unique = set(nums)
        for i in unique:
            if i > 0:
                s += i
        if s == 0:
            return max(nums)
        return s

# Time Complexity: O(N)
# Space Complexity: O(1)