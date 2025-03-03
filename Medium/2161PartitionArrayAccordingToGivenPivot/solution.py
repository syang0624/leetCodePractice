from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        pvt = []

        for n in nums:
            if n < pivot:
                less.append(n)
            elif n > pivot:
                greater.append(n)
            else:
                pvt.append(n)
        
        return less+pvt+greater
    
# Time Complexity: O(N)
# Space Complexity: O(N)