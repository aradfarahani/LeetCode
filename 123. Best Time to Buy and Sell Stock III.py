class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        left_profits = [0] * n
        right_profits = [0] * n
        
        # Calculate max profit for one transaction from the left
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)
        
        # Calculate max profit for one transaction from the right
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profits[i] = max(right_profits[i + 1], max_price - prices[i])
        
        # Calculate the maximum profit by combining the two transactions
        max_profit = 0
        for i in range(n):
            max_profit = max(max_profit, left_profits[i] + right_profits[i])
        
        return max_profit
