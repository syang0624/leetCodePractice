from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        time, fresh = 0, 0
        queue = []

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r, c])

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue and fresh > 0:
            for x in range(len(queue)):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row < 0
                        or row == m
                        or col < 0
                        or col == n
                        or grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    fresh -= 1
                    queue.append([row, col])
            time += 1

        if fresh == 0:
            return time
        else:
            return -1


# Time: O(M*N)
# Space: O(M*N)
