# Time: O(n)
# Space: O(n)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)

        for i in range(len(nums)):
            j = -i - 1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = l_arr[i] * r_arr[i]
        return result
