from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) Bubble Sort Solution
        # count = {}
        # frequency = [[] for x in range(len(nums)+1)]

        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # for n, c in count.items():
        #     frequency[c].append(n)

        # result = []
        # for i in range(len(frequency)-1, -1, -1):
        #     for _ in frequency[i]:
        #         result.append(_)
        #         if len(result) == k:
        #             return result
        # O(n log k) Min Heap Solution
        counter = Counter(nums)
        heap = [(v, k) for (k, v) in counter.items()]
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        return [num for (freq, num) in heap]
