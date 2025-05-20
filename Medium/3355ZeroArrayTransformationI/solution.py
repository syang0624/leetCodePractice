from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # TLE Solution
        # for i in queries:
        #     l, r = i[0], i[1]
        #     for j in range(l, r+1):
        #         if nums[j] != 0:
        #             nums[j] -= 1
        
        # return True if set(nums) == {0} else False
        deltaArray = [0] * (len(nums) + 1)
        for left, right in queries:
            deltaArray[left] += 1
            deltaArray[right + 1] -= 1
        operationCounts = []
        currentOperations = 0
        for delta in deltaArray:
            currentOperations += delta
            operationCounts.append(currentOperations)
        for operations, target in zip(operationCounts, nums):
            if operations < target:
                return False
        return True
    
# Time Complexity: O(N+M)
# Space Complexity: O(N)