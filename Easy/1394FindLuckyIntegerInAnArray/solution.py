from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        max_res = -1
        for k in count:
            if k == count[k]:
                max_res = max(max_res, k)
        return max_res
    
# Time Complexity: O(N)
# Space Complexity: O(N)