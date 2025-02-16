from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for a in arr:
            if a in count:
                count[a] += 1
            else:
                count[a] = 1
        return len(set(count.values())) == len(count)

# Time Complexity: O(N)
# Space Complexity: O(N)