class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # TLE solution
        # maxCount = 0
        # vowels = [ 'a', 'e', 'i', 'o', 'u']
        # for i in range(0, len(s)-k+1):
        #     lst = s[i:i+k]
        #     localCount = 0
        #     for j in range(len(lst)):
        #         if lst[j] in vowels:
        #             localCount += 1
        #     maxCount = max(maxCount, localCount)
        #     if maxCount == k:
        #         break
        # return maxCount
        vowels = ["a", "e", "i", "o", "u"]
        maxCount, localCount, left = 0, 0, 0
        for right in range(len(s)):
            localCount += 1 if s[right] in vowels else 0
            if right - left + 1 > k:
                localCount -= 1 if s[left] in vowels else 0
                left += 1
            maxCount = max(maxCount, localCount)

        return maxCount
