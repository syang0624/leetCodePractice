class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for a in s:
            if a == "*":
                stack.pop()
            else:
                stack.append(a)
        return "".join(stack)