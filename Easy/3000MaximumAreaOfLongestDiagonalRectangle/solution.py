from typing import List
import math
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonal = 0
        maxArea = 0
        for l, w in dimensions:
            diagonal = math.sqrt(l**2 + w**2)
            area = l * w
            if diagonal > maxDiagonal:
                maxDiagonal = diagonal
                maxArea = area
            elif diagonal == maxDiagonal:
                maxArea = max(maxArea, area)
        
        return maxArea

# Time Complexity: O(N)
# Space Complexity: O(1)