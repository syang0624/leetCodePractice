from typing import List
from collections import Counter

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        best = 0
        left = 0
        freq = Counter()
        for right in range(N):
            freq[nums[right]] += 1
            total += nums[right]
            while freq[nums[right]] > 1:
                freq[nums[left]] -= 1
                total -= nums[left]
                left += 1
            best = max(best, total)
        return best

# Time Complexity: O(N)
# Space Complexity: O(N)