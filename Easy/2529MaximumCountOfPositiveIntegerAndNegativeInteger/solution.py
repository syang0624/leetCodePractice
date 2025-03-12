from typing import List

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg = 0
        pos = 0
        for i in range(n):
            if nums[i] > 0:
                pos = n - i
                return max(neg, pos)
            if nums[i] < 0:
                neg += 1
        
        return max(neg, pos)

# Time Complexity O(N)
# Space Complexity O(1)