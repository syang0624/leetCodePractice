from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count = Counter(s)
        odd = 0 
        for cnt in count.values():
            odd += cnt % 2
        return odd <= k
    


# Time: O(n)
# Space: O(n)