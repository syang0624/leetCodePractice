from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        h = 0
        for i in range(len(citations)):
            temp = len(citations) - i
            if citations[i] >= temp:
                h = max(h, temp)
        return h

# Time Complexity: O(N log N)
# Space Complexity: O(1)