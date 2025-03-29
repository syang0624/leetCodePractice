from typing import List
from math import sqrt
from heapq import heapify, heappop


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        res = 1

        prime_scores = []
        for n in nums:
            score = 0
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n = n // f
            if n >= 2:
                score += 1
            prime_scores.append(score)

        
        left_bound = [-1] * N
        right_bound = [N] * N

        stack = []
        for i, s in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < s:
                index = stack.pop()
                right_bound[index] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)
        
        min_heap = [(-n, i) for i, n in enumerate(nums)]
        heapify(min_heap)

        while k > 0:
            n, index = heappop(min_heap)
            n = -n
            score = prime_scores[index]

            left_cnt = index - left_bound[index]
            right_cnt = right_bound[index] - index

            count = left_cnt * right_cnt
            operations = min(count, k)
            res = (res * pow(n, operations, MOD)) % MOD
            k -= operations
        
        return res

# Time Complexity: O(N√M + k log N)
# Space Complexity: O(N)