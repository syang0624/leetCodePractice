from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums = sorted(nums)
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        length = len(set(nums))
        if length == 3:
            return "scalene"
        elif length == 2:
            return "isosceles"
        else:
            return "equilateral"

# Time Complexity: O(1)
# Space Complexity: O(1)