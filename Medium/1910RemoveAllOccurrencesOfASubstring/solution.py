class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for a in s:
            stack.append(a)
            if len(stack) >= n and "".join(stack[-n:]) == part:
                    for _ in range(n):
                        stack.pop()
        return "".join(stack)
    
# Time Complexity: O(N)
# Space Complexity: O(N)