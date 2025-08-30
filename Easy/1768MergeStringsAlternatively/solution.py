class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0
        while i < len(word1) and i < len(word2):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1

        merged.append(word1[i:])
        merged.append(word2[i:])

        return "".join(merged)

# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         res = ""
#         while word1 and word2:
#             if word1:
#                 res = res + word1[0]
#                 word1 = word1[1:]
#             if word2:
#                 res = res + word2[0]
#                 word2 = word2[1:]
#         res = res + word1 + word2
#         return res