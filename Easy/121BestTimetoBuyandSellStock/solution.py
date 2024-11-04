from typing import List


# class Solution:
#     # Two pointers
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = prices[0]
#         max_price = 0
#         for a in prices[1:]:
#             max_price = max(max_price, a - min_price)
#             min_price = min(min_price, a)
#         return max_price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit
