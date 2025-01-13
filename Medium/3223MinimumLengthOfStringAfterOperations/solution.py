from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        arr = []
        for v in Counter(s).values():
            if v >= 2 and v % 2 == 0:
                arr.append(2)
            elif v >= 2 and v % 2 != 0:
                arr.append(1)
            else:
                arr.append(v)
        return sum(arr)
    
# Time: O(N)
# Space: O(N)