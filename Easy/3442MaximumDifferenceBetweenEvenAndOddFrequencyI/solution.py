from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        unique = Counter(s)
        odd = max(unique[c] for c in unique if unique[c] % 2 != 0)
        even = min(unique[c] for c in unique if unique[c] % 2 == 0)
        return odd - even

# Time Complexity: O(N)
# Space Complexity: O(N)