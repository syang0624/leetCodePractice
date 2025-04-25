from typing import List
from collections import Counter

class Solution:
    def countInterestingSubarrays(
        self, nums: List[int], modulo: int, k: int
    ) -> int:
        n = len(nums)
        cnt = Counter([0])
        res = 0
        prefix = 0
        for i in range(n):
            prefix += 1 if nums[i] % modulo == k else 0
            res += cnt[(prefix - k + modulo) % modulo]
            cnt[prefix % modulo] += 1
        return res
    
# Time Complexity: O(N)
# Space Complexity: O(N)