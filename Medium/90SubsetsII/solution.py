from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # nums.sort()

        # subset = []

        # def dfs(i):
        #     if i >= len(nums):
        #         if subset.copy() not in res:
        #             res.append(subset.copy())
        #         return

        #     subset.append(nums[i])
        #     dfs(i + 1)

        #     subset.pop()
        #     dfs(i + 1)

        # dfs(0)
        # return res
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res
