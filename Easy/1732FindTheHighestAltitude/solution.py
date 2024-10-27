from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = 0
        curAlt = 0
        for x in range(len(gain)):
            curAlt += gain[x]
            maxAlt = max(maxAlt, curAlt)
        return maxAlt
