class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = sell - buy
        # curr i - sell
        # to left - buy
        # if all values to left produce negative profit we skip and return 0

        stack = []
        max_profit = 0
        for i in range(len(prices)):
            if not stack:
                stack.append(prices[i])
            
            if prices[i] < stack[-1]:
                stack.append(prices[i])
            else:
                profit = prices[i] - stack[-1]
                max_profit = max(max_profit, profit)
                j = -1
                while -1 * j < len(stack) - 1 and stack[j] < prices[i]:
                    j -= 1
                stack.insert(j, prices[i])

        return max_profit
