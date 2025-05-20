from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = []
        # strs = sorted(strs)
        # for a in strs[0]:
        #     for b in strs:
        #         if a != b[len(res)]:
        #             return str("".join(res))
        #     res.append(a)
        # return str("".join(res))

        if len(strs) == 0:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return ""
        return prefix
# Time Complexity: O(S) where S is the sum of all characters in all strings
# Space Complexity; O(1)