from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        h = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(h)

        return [heapq.heappop(h)[1] for _ in range(k)]

# Time Complexity: O(k log n)
# Space Complexity: O(n)