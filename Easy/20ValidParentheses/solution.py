
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")": "(", "]": "[", "}": "{"}

        for a in s:
            if a in hashmap.values():
                stack.append(a)
            elif a in hashmap.keys():
                if not stack or hashmap[a] != stack.pop():
                    return False
        return not stack
