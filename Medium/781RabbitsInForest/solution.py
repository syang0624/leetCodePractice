import collections
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        f = collections.Counter(answers)
        
        total = 0
        for k in f.keys():
            total += ((f[k] + k) // (k + 1)) * (k + 1)
        
        return total

# Time Complexity: O(N)
# Space Complexity: O(N)