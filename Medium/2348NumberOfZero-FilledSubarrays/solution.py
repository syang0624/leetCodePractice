from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i, res = 0, 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 0:
                count += 1
                i += 1
                res += count
            i += 1
        return res

# Time Complexity: O(N)
# Space Complexity: O(1)