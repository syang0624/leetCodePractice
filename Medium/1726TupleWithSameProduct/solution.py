from typing import List

from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        freq = defaultdict(int)  # K -> product, V -> frequency of such pair


        for i in range(n - 1):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                freq[product] += 1

        count = 0
        for frequency in freq.values():
            count += 8 * ((frequency * (frequency - 1)) // 2)

        return count
    

# Time Complexity : O(N^2)
# Space Complexity : O(N^2)