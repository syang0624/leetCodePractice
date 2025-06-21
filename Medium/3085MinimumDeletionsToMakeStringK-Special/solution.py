from collections import defaultdict

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        cnt = defaultdict(int)
        for c in word:
            cnt[c] += 1
        ans = len(word)
        for a in cnt.values():
            deleted = 0
            for b in cnt.values():
                if a > b:
                    deleted += b
                elif b > a + k:
                    deleted += b - (a + k)
            ans = min(ans, deleted)
        return ans

# Time Complexity: O(26^2)
# Space Complexity: O(26)