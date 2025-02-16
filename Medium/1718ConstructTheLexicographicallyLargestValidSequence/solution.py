from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2*n - 1)
        used = set()

        def backtrack(i):
            if i == len(res):
                return True
            # For greedy purpose, try the largest element first.
            for num in reversed(range(1, n+1)):
                # Validation
                if num in used:
                    continue
                if num > 1 and (i+num >= len(res) or res[i+num]):
                    continue
                # Try if it works
                used.add(num)
                res[i] = num
                if num > 1:
                    res[i+num] = num
                j = i + 1
                while j < len(res) and res[j]:
                    j += 1
                # Recursive Calls
                if backtrack(j):
                    return True
                # Backtracking
                used.remove(num)
                res[i] = 0
                if num > 1:
                    res[i+num] = 0
            return False
        
        backtrack(0)
        return res

# Time Complexity: O(N!)
# Space Complexity: O(N)