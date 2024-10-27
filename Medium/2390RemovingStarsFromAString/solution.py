class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        s.split()
        for x in s:
            if x != "*":
                stack.append(x)
            else:
                stack.pop()
        return "".join(stack)
