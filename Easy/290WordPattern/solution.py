class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        storage = {}
        used = set()
        s = list(s.split(" "))
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in storage:
                if s[i] in used:
                    return False
                storage[pattern[i]] = s[i]
                used.add(s[i])
            else:
                if storage[pattern[i]] != s[i]:
                    return False
        return True

# Time Complexity: O(N)
# Space Complexity: O(N)