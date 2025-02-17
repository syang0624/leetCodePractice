from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)
        def backtracking():
            res = 0
            for char in count:
                if count[char] == 0:
                    continue
                else:
                    count[char] -= 1
                    res += 1
                    res += backtracking()
                    count[char] += 1
            return res

        
        return backtracking()
# Time Complexity: O(k^n)
# Space Complexity: O(n)