class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        max_profit = l = 0
        for r in range(1, len(prices)):
            while l < r and prices[l] > prices[r]:
                l += 1
            max_profit = max(prices[r] - prices[l], max_profit)
        return max_profit
        