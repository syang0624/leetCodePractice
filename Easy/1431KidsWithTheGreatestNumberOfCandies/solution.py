from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxChild = max(candies)
        diff = maxChild - extraCandies
        for i in range(len(candies)):
            if maxChild - candies[i] > extraCandies:
                candies[i] = False
            else:
                candies[i] = True
        return candies

# Time Complexity: O(N)
# Space Complexity: O(1)