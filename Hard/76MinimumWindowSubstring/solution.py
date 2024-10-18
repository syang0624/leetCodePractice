from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        overall = len(c)

        left = 0
        right = 0
        res = ""

        while right < len(s):
            if s[right] in c:
                c[s[right]] -= 1
                if c[s[right]] == 0:
                    overall -= 1
            while overall == 0:
                if not res:
                    res = s[left : right + 1]
                elif len(s[left : right + 1]) < len(res):
                    res = s[left : right + 1]
                if s[left] in c:
                    c[s[left]] += 1
                    if c[s[left]] > 0:
                        overall += 1
                left += 1

            right += 1

        return res
