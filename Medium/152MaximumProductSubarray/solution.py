from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currentMax, currentMin = 1, 1
        for n in nums:
            if n == 0:
                currentMax, currentMin = 1, 1
                continue
            else:
                temp = n * currentMax
                currentMax = max(n * currentMax, n * currentMin, n)
                currentMin = min(temp, n * currentMin, n)
            res = max(res, currentMax)

        return res
