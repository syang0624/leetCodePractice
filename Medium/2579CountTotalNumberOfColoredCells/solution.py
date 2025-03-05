class Solution:
    def coloredCells(self, n: int) -> int:
        # res = 1
        # count = 1
        # while count != n:
        #     res += (4 * count)
        #     count += 1
        # return res
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        
        return n * (n - 1) * 2 + 1

# Time Complexity: O(1)
# Space Complexity: O(1)