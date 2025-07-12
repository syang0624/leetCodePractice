from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        expressions = ['+', '-', '*', '/']
        stack = []
        for a in tokens:
            if a not in expressions:
                stack.append(a)
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if a == "*":
                    res = y * x
                elif a == "/":
                    res = int(y / x)
                elif a == "+":
                    res = y + x
                else:
                    res = y - x
                stack.append(res)
        return int(stack[0])

# Time Complexity: O(N)
# Space Complexity: O(N)