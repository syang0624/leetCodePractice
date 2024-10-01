from typing import List


class Solution:
    # Two pointers
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0
        for a in prices[1:]:
            max_price = max(max_price, a - min_price)
            min_price = min(min_price, a)
        return max_price