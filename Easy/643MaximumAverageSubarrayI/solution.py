from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # TLE solution
        # maxSum = float('-inf')
        # for x in range(len(nums)):
        #     if len(nums[x:x+k]) < k:
        #         break
        #     maxSum = max(maxSum, sum(nums[x:x+k]))

        # return maxSum / k
        n = len(nums)
        curSum = 0

        for i in range(k):
            curSum += nums[i]
        maxAvg = curSum / k

        for j in range(k, n):
            curSum += nums[j]
            curSum -= nums[j - k]
            maxAvg = max(maxAvg, curSum / k)

        return maxAvg
