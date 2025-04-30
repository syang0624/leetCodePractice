from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                count += 1
        return count
    

# Time Complexity: O(N)
# Space Complexity: O(1)