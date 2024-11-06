# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # globalMax = nums[0]
        # localMax = nums[0]

        # for i in range(1, len(nums)):
        #     localMax = max(nums[i], localMax + nums[i])
        #     globalMax = max(globalMax, localMax)

        # return globalMax
        maxSum = nums[0]
        currentSum = 0
        for n in nums:
            currentSum += n
            maxSum = max(maxSum, currentSum)
            if currentSum < 0:
                currentSum = 0
        return maxSum
