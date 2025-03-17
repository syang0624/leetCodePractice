from typing import List
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        res = 0
        for v in count.values():
            print(v)
            if v % 2 != 0:
                return False
            else:
                res += int(v // 2)
        return res == len(nums) // 2

# Time Complexity: O(N)
# Space Complexity: O(N)