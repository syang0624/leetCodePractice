from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = [[entrance[0], entrance[1], 0]]
        maze[entrance[0]][entrance[1]] = "+"
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j, steps = queue.pop(0)
            if i == 0 or i == len(maze) - 1 or j == 0 or j == len(maze[0]) - 1:
                if steps > 0:
                    return steps
            for di, dj in directions:
                if (
                    0 <= i + di < len(maze)
                    and 0 <= j + dj < len(maze[0])
                    and maze[i + di][j + dj] == "."
                ):
                    queue.append([i + di, j + dj, steps + 1])
                    maze[i + di][j + dj] = "+"

        return -1


# Time: O(M*N)
# Space: O(M*N)
