class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rst = []
        for x in range(len(words) - 1, -1, -1):
            rst.append(words[x])

        return " ".join(rst)
