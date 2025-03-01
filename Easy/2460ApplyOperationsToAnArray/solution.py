from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        res = []
        for x in nums:
            if x != 0:
                res.append(x)
        for a in range(len(nums) - len(res)):
            res.append(0)

        return res
    
# Time Complexity: O(N)
# Time Complexity: O(1)