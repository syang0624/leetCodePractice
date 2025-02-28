class Solution:
    # # Memory Limit Exceeded Solution
    # def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    #     cache = {}

    #     def backtrack(i, j):
    #         if (i, j) in cache:
    #             return cache[(i,j)]
    #         if i == len(str1):
    #             return str2[j:]
    #         if j == len(str2):
    #             return str1[i:]
            
    #         if str1[i] == str2[j]:
    #             return str1[i] + backtrack(i+1, j+1)
            

    #         res1 = str1[i] + backtrack(i+1, j)
    #         res2 = str2[j] + backtrack(i, j+1)
    #         if len(res1) < len(res2):
    #             cache[(i,j)] = res1
    #             return res1
    #         cache[(i,j)] = res2
    #         return res2

        
    #     return backtrack(0,0)
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # ChatGPT DP Solution
        m, n = len(str1), len(str2)

        # Step 1: Compute LCS using DP
        dp = [[""] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

        # Step 2: Build the shortest common supersequence using LCS
        i, j = 0, 0
        result = []
        for c in dp[m][n]:  # Traverse LCS string
            while i < m and str1[i] != c:
                result.append(str1[i])
                i += 1
            while j < n and str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i, j = i + 1, j + 1

        # Append remaining parts of str1 and str2
        result.append(str1[i:])
        result.append(str2[j:])

        return "".join(result)
    
# Time Complexity: O(MN)
# Space Complexity: O(MN)