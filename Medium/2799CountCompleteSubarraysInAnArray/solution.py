from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_elements = set(nums)
        unique_count = len(unique_elements)
        
        left = 0
        right = 0
        n = len(nums)
        freq = {}
        complete_subarrays = 0
        
        while left < n:
            while right < n and len(freq) < unique_count:
                freq[nums[right]] = freq.get(nums[right], 0) + 1
                right += 1
            
            if len(freq) < unique_count:
                break
            
            complete_subarrays += n - right + 1
            
            # Remove left
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1
        
        return complete_subarrays
    
# Time Complexity: O(N)
# Space Complexity: O(N)