from typing import List
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((w, v))
            adj[v].append((w, u))
        MOD = 10**9 + 7
        min_heap = [(0, 0)] # (cost, node)
        min_cost = [float("inf")] * n
        path_count = [0] * n
        path_count[0] = 1
        while min_heap:
            cost, node = heappop(min_heap)
            for nei_cost, nei in adj[node]:
                if cost + nei_cost < min_cost[nei]:
                    min_cost[nei] = cost + nei_cost
                    path_count[nei] = path_count[node]
                    heappush(min_heap, (cost + nei_cost, nei))
                elif cost + nei_cost == min_cost[nei]:
                    path_count[nei] = (path_count[nei] + path_count[node]) % MOD
        return path_count[n-1]
    
# Time Complexity: O((V+E) log V)
# Space Complexity: O(V+E)