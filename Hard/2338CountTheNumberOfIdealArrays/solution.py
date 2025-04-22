from collections import defaultdict
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7
        maxLen = min(n, 14)  # max chain length (log2(maxValue) at most)

        # dp[k][v] = number of chains of length k ending at value v
        dp = [defaultdict(int) for _ in range(maxLen + 1)]
        
        # base case: chains of length 1
        for v in range(1, maxValue + 1):
            dp[1][v] = 1

        # build up chains of increasing length
        for length in range(2, maxLen + 1):
            for v in range(1, maxValue + 1):
                for m in range(2 * v, maxValue + 1, v):
                    dp[length][m] = (dp[length][m] + dp[length - 1][v]) % MOD

        # precompute factorials for combinations
        fact = [1] * (n + 1)
        inv_fact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        # nCk function using precomputed factorials
        def nCk(n, k):
            if k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        # sum up all valid configurations
        result = 0
        for length in range(1, maxLen + 1):
            for v in dp[length]:
                count = dp[length][v]
                result = (result + count * nCk(n - 1, length - 1)) % MOD

        return result

# Time Complexity: O(n * log(maxValue)^2 + maxValue * log(maxValue))
# Space Complexity: O(n + log(maxValue) * maxValue)