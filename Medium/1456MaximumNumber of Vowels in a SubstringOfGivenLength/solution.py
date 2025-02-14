class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        left, maxCount, count = 0, 0, 0
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    count -= 1
                left += 1
            maxCount = max(maxCount, count)
        return maxCount