class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack: stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)
    
# Time Complexity: O(N)
# Space Complexity: O(N)