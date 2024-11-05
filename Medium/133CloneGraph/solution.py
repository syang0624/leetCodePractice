from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return None

    #     start = node
    #     oldToNew = {}
    #     stack = [start]
    #     visited = set()
    #     visited.add(start)

    #     while stack:
    #         node = stack.pop()
    #         oldToNew[node] = Node(node.val)

    #         for nei in node.neighbors:
    #             if nei not in visited:
    #                 visited.add(nei)
    #                 stack.append(nei)

    #     for old, new in oldToNew.items():
    #         for nei in old.neighbors:
    #             newNei = oldToNew[nei]
    #             new.neighbors.append(newNei)

    #     return oldToNew[start]
    # DFS Helper Function Solution
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        if node:
            return dfs(node)
        else:
            return None


# Time: O(N+E)
# Space: O(N)
