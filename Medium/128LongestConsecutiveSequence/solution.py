from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set(nums)
        # longest = 0
        # for n in nums:
        #     if (n-1) not in numSet:
        #         length = 0
        #         while (n+length) in numSet:
        #             length += 1
        #         longest = max(longest, length)
        # return longest
        if not nums:
            return 0

        sorted_nums = sorted(set(nums))

        longest = 1
        best = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                best += 1
            else:
                longest = max(longest, best)
                best = 1

        return max(longest, best)
