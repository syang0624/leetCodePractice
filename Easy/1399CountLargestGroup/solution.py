import collections

class Solution:
    def countLargestGroup(self, n: int) -> int:
        count = collections.Counter()
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            count[key] += 1
        maxValue = max(count.values())
        result = sum(1 for v in count.values() if v == maxValue)
        return result

# Time Complexity: O(n log n)
# Space Complexity: O(log n)