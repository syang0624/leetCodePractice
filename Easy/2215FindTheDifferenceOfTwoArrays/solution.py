from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one = set(nums1) - set(nums2)
        two = set(nums2) - set(nums1)
        return [list(one), list(two)]

# M = len(nums1), N = len(nums2)
# Time Complexity: O(M + N)
# Space Complexity: O(M + N)