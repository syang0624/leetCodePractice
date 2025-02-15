class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(idx, cur, target, string):
            if idx == len(string) and cur == target:
                return True
            for j in range(idx, len(string)):
                if partition(j + 1, cur + int(string[idx:j+1]), target, string):
                    return True
            return False
        
        res = 0
        for i in range(1, n + 1):
            if partition(0, 0, i, str(i * i)):
                res += i * i
        return res
    
# Time Complexity: O(N^2)
# Space Complexity: O(N)