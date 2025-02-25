from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix_sum = 0
        odd_cnt = 0
        even_cnt = 0
        res = 0
        MOD = 10**9 + 7

        for n in arr:
            prefix_sum += n
            if prefix_sum % 2:
                res = (res + 1 + even_cnt) % MOD
                odd_cnt += 1
            else:
                res = (res + odd_cnt) % MOD
                even_cnt += 1
        return res
    
# Time Complexity: O(N)
# Space Complexity: O(N)