from typing import List
from collections import defaultdict

class Solution:
    def getDigitSum(self, val: int) -> int:
        digitSum = 0
        while val:
            digitSum += val % 10
            val //= 10
        return digitSum

    def maximumSum(self, nums: List[int]) -> int:
        sum_maxval = defaultdict(int)
        max_sum = -1

        for element in nums:
            digitSum = self.getDigitSum(element)
            if digitSum in sum_maxval:
                max_sum = max(max_sum, element + sum_maxval[digitSum])
                if sum_maxval[digitSum] < element:
                    sum_maxval[digitSum] = element
            else:
                sum_maxval[digitSum] = element
        return max_sum
    
# Time Complexity: O(N)
# Space Complexity: O(N)