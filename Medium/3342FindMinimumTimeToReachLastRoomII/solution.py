import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        dir = [-1, 0, 1, 0 , -1]
        
        def isValid(r, c, m, n):
            return 0 <= r < m and 0 <= c < n
        
        minHeap = [(0, 0, 0, 1)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        

        while minHeap:
            time, r, c, cost = heapq.heappop(minHeap)
            
            if r == m - 1 and c == n - 1:
                return time
            
            for i in range(4):
                newR, newC = r + dir[i], c + dir[i+1]
                nextCost = 2 if cost == 1 else 1
                if isValid(newR, newC, m, n) and not visited[newR][newC]:
                    newTime = cost + max(time, moveTime[newR][newC])    
                    heapq.heappush(minHeap, (newTime, newR, newC, nextCost))
                    visited[newR][newC] = True
        
        return -1

# Time Complexity: O(mn * log(mn))
# Space Complexity: O(mn)