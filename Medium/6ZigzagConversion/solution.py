class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        globalIdx = 0
        n = len(s)
        
        while globalIdx < n:
            for i in range(numRows):
                if globalIdx < n:
                    res[i].append(s[globalIdx])
                    globalIdx += 1
            for j in range(numRows - 2, 0, -1):
                if globalIdx < n:
                    res[j].append(s[globalIdx])
                    globalIdx += 1
        answer = ""
        for row in res:
            answer += ''.join(row)
        return answer

# Time Complexity: O(N)
# Space Complexity: O(N)