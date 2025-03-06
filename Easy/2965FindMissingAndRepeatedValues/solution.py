from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        maxNum = len(grid) * len(grid)
        hash_table = {key: 2 for key in range(1, maxNum+1)}
        for x in range(len(grid)):
            for y in range(len(grid)):
                hash_table[grid[x][y]] -= 1
        rep = 0
        miss = 0
        
        for k, v in hash_table.items():
            if v == 0:
                rep = k
            if v == 2:
                miss = k
        
        return [rep, miss]

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
