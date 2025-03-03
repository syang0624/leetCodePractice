from typing import List


# class Solution:
    # Brute Force
    # Time O(N^2)
    # Space O(1)
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for x in range(len(nums)):
    #         for y in range(x+1, len(nums)):
    #             if nums[x] + nums[y] == target:
    #                 return [x, y]


    

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
    # Time O(N)
    # Space O(N)