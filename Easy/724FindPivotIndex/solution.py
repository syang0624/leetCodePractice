from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumLeft = 0
        total = sum(nums)
        for i in range(len(nums)):
            sumRight = total - sumLeft - nums[i]
            if sumLeft == sumRight:
                return i
            sumLeft += nums[i]
        return -1
    
# Time Complexity: O(N)
# Space Complexity: O(1)