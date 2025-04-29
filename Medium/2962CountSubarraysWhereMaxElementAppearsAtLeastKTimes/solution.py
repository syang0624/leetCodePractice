from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        start, sub_count, ans = 0, 0, 0

        for end in range(len(nums)):
            if nums[end] == max_element:
                sub_count += 1
            while sub_count == k:
                if nums[start] == max_element:
                    sub_count -= 1
                start += 1
            ans += start
        return ans