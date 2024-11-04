from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = []
        stack = []
        visited.append(0)
        for x in rooms[0]:
            stack.append(x)
        while stack:
            s = stack.pop()
            if s not in visited:
                visited.append(s)
                for x in rooms[s]:
                    stack.append(x)
        if len(visited) == len(rooms):
            return True
        else:
            return False