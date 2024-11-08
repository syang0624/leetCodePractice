from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Brute Force Solution
        # perimeter = 0
        # for x in range(len(grid)):
        #     for y in range(len(grid[0])):
        #         if grid[x][y] == 1:
        #             perimeter += 4
        #             if x + 1 < len(grid) and grid[x+1][y] == 1:
        #                 perimeter -= 2
        #             if y + 1 < len(grid[0]) and grid[x][y+1] == 1:
        #                 perimeter -= 2

        # return perimeter
        # Time: O(MN) Space: O(1)

        # DFS Solution
        visit = set()

        def dfs(x, y):
            perimeter = 0
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0 or grid[x][y] == 0:
                return 1
            if (x, y) in visit:
                return 0
            visit.add((x, y))
            perimeter += dfs(x + 1, y)
            perimeter += dfs(x - 1, y)
            perimeter += dfs(x, y + 1)
            perimeter += dfs(x, y - 1)
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        # Time: O(MN) Space: O(MN)
