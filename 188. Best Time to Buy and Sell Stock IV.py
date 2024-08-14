class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0
        
        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        
        return dp[k][n - 1]

# Example usage:
solution = Solution()
print(solution.maxProfit(2, [2, 4, 1]))  # Output: 2
print(solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))  # Output: 7
