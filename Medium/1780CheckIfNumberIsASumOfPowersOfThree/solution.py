class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        # def backtrack(i, cur):
        #     if cur == n:
        #         return True
        #     if cur > n or 3**i > n:
        #         return False
        #     # include
        #     if backtrack(i + 1, cur + 3**i):
        #         return True
        #     # skip
        #     return backtrack(i + 1, cur)
        
        # return backtrack(0, 0)
        i = 0
        while 3**i < n:
            i += 1
        while i >= 0:
            if 3 ** i <= n:
                n -= (3 ** i)
            i -= 1
        return n == 0

# Time Complexity: O(log 3 n)
# Space Complexity: O(1)