import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Max Heap Solution
        # for i in range(len(nums)):
        #     nums[i] = -nums[i]

        # heapq.heapify(nums)

        # for _ in range(k-1):
        #     heapq.heappop(nums)

        # return -heapq.heappop(nums)

        # Min Heap Solution
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]


# Tiime: O(N + klogN)
# heapify takes O(N) time and heapop takes O(logN) time but for k-1 times

# Space: O(1)
