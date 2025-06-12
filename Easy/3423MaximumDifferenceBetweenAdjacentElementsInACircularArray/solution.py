from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff = abs(nums[0] - nums[-1])
        for i in range(0, len(nums) - 1):
            cur = abs(nums[i] - nums[i + 1])
            if cur > diff:
                diff = cur
        
        return diff

# Time Complexity: O(N)
# Space Complexity: O(1)