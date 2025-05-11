from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for n in arr:
            if n % 2 != 0:
                count += 1
            else:
                count = 0
            if count == 3:
                return True
        return False

# Time Complexity: O(N)
# Space Complexity: O(1)