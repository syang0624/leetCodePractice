"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        start = node
        oldToNew = {}
        stack = [start]
        visited = set()
        visited.add(start)

        while stack:
            node = stack.pop()
            oldToNew[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        for old, new in oldToNew.items():
            for nei in old.neighbors:
                newNei = oldToNew[nei]
                new.neighbors.append(newNei)

        return oldToNew[start]
