class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        storage = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in storage:
                if t[i] in used:
                    return False
                storage[s[i]] = t[i]
                used.add(t[i])
            else:
                if storage[s[i]] != t[i]:
                    return False
        return True

# Time Complexity: O(N)
# Space Complexity: O(N)