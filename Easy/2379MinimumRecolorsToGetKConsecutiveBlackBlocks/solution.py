class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = float("inf")
        for x in range(len(blocks) - k + 1):
            whites = 0
            for y in range(x, x+k):
                if blocks[y] == "W":
                    whites += 1
            count = min(count, whites)
        return count

# Time Complexity O(N*K)
# Space Complexity O(1)