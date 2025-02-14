from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        maxAltitude = 0
        for a in gain:
            current += a
            maxAltitude = max(maxAltitude, current)
        return maxAltitude