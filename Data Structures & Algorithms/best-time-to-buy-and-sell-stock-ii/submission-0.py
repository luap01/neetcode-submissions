class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        bought = None

        stack = []
        for price in prices:
            if bought is None:
                bought = price
            elif price < bought:
                bought = price
            else:
                max_profit += price - bought
                bought = price
        
        return max_profit