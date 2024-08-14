class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = dp[m-1][n] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(min_health_on_exit - dungeon[i][j], 1)
        
        return dp[0][0]

# Example usage:
solution = Solution()
print(solution.calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # Output: 7
print(solution.calculateMinimumHP([[0]]))  # Output: 1
