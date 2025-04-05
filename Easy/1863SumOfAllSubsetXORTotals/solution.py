from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num
        return result << (len(nums) - 1)

# Time Complexity: O(N)
# Space Complexity: O(1)