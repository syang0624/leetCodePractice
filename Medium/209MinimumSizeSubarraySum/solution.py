# Time: O(N)
# Space: O(1)

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        if min_length < float('inf'):
            return min_length
        else:
            return 0