from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        for i, num in enumerate(nums):
            if num in hashMap and abs(i - hashMap[num]) <= k:
                return True
            else:
                hashMap[num] = i
        return False

# Time Complexity: O(N)
# Space Complexity: O(N)