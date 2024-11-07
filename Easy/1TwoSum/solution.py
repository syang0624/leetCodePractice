from typing import List


class Solution:
    # Brute Force
    # Time O(N^2)
    # Space O(1)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for x in range(len(nums)):
    #         for y in range(x+1, len(nums)):
    #             if nums[x] + nums[y] == target:
    #                 return [x, y]

    # HashMap
    # Time O(N)
    # Space O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for x in range(len(nums)):
            hashMap[nums[x]] = x
        for i in range(len(nums)):
            y = target - nums[i]
            if y in hashMap and hashMap[y] != i:
                return [i, hashMap[y]]
