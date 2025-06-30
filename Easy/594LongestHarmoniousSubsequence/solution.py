from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_length = 0

        for num in count:
            if num + 1 in count:
                max_length = max(max_length, count[num] + count[num + 1])

        return max_length

# Time Complexity: O(N)
# Space Complexity: O(N)