from typing import List
from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        q = deque()
        q.append([startGene, 0])
        visited = set()
        visited.add(startGene)

        while q:
            gene, level = q.popleft()
            if gene == endGene:
                return level
            for i in range(len(gene)):
                for letter in "ACGT":
                    new = gene[:i] + letter + gene[i+1:]
                    if new not in visited and new in bank:
                        q.append([new, level + 1])
                        visited.add(new)
        return -1

# Time Complexity: O(MN)
# Space Complexity: O(N)