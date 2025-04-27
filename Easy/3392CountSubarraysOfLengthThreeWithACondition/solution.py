from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for a in range(len(nums) - 2):
            if (nums[a] + nums[a + 2]) * 2 == nums[a + 1]:
                count += 1
        return count
    
# Time Complexity: O(N)
# Space Complexity: O(1)