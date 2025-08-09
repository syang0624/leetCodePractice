class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for a in range(-31,32):
            if 2**a == n:
                return True
        return False