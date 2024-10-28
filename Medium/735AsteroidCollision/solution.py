from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                difference = stack[-1] + a
                if difference == 0:
                    stack.pop()
                    a = 0
                elif difference < 0:
                    stack.pop()
                else:
                    a = 0
            if a:
                stack.append(a)

        return stack
