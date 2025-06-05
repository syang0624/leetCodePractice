from typing import List

class Solution:

  def check(self, num: int, count: int) -> int:
    if num == 1:
      if count < 2 or count > 3:
        return 2
      else:
        return 1
    if num == 0 and count == 3:
      return -1
    else:
      return 0

  def gameOfLife(self, board: List[List[int]]) -> None:
    """
      Do not return anything, modify board in-place instead.
    """
    ROWS, COLS = len(board), len(board[0])

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1),
            (-1, -1)]
    for r in range(ROWS):
      for c in range(COLS):
        count = 0
        for dr, dc in dirs:
          if r + dr >= 0 and r + dr < ROWS and c + dc >= 0 and c + dc < COLS:
            if board[r + dr][c + dc] >= 1:
              count += 1
        board[r][c] = self.check(board[r][c], count)
    for r in range(ROWS):
      for c in range(COLS):
        if board[r][c] == 2:
          board[r][c] = 0
        if board[r][c] == -1:
          board[r][c] = 1

# Time Complexity: O(1)
# Space Complexity: O(1)