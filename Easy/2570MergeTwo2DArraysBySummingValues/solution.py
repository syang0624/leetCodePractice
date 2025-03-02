from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dictionary = {}
        for a, b in nums1:
            dictionary[a] = b
        for a, b in nums2:
            if a in dictionary.keys():
                dictionary[a] += b
            else:
                dictionary[a] = b
        
        res = []
        for k in dictionary.keys():
            res.append([k, dictionary[k]])
        return sorted(res)
    
# Time Complexity: O(N1 + N2)
# Space Complexity: O(N1 + N2)