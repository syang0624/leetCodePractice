from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove consecutive equal elements to get the true "peaks" and "valleys"
        unique_nums = []
        for i in range(len(nums)):
            if not unique_nums or nums[i] != unique_nums[-1]:
                unique_nums.append(nums[i])
        
        count = 0
        # Loop through the modified list of unique values
        for i in range(1, len(unique_nums) - 1):
            if unique_nums[i - 1] < unique_nums[i] > unique_nums[i + 1]:
                count += 1  # It's a hill
            elif unique_nums[i - 1] > unique_nums[i] < unique_nums[i + 1]:
                count += 1  # It's a valley

        return count

# Time Compleixty: O(N)
# Space Compleixty: O(N)