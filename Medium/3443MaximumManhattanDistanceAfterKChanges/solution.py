class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        maxManhattan = 0
        latitude = 0
        longitude = 0

        n = len(s)

        for i in range(n):
            if s[i] == "N":
                latitude += 1
            elif s[i] == "S":
                latitude -= 1
            elif s[i] == "E":
                longitude += 1
            elif s[i] == "W":
                longitude -= 1
            maxManhattan = max(maxManhattan, min(abs(latitude) + abs(longitude) + k * 2, i + 1))
        return maxManhattan

# Time Complexity: O(N)
# Space Complexity: O(1)