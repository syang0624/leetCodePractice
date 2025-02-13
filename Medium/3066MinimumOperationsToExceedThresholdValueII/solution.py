from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        number_of_operations = 0
        heapq.heapify(nums)
        while nums[0] < k:
            number_of_operations += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
        return number_of_operations
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)