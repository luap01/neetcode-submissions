class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            profit = sell - min_buy
            max_profit = max(max_profit, profit)
            min_buy = min(min_buy, sell)

        return max_profit
