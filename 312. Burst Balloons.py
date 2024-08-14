class Solution:
    def maxCoins(self, nums):
        # Add 1 before and after nums to handle edge cases
        nums = [1] + nums + [1]
        n = len(nums)
        
        # Create a DP table
        dp = [[0] * n for _ in range(n)]
        
        # Fill the DP table
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        
        return dp[0][n - 1]

# Example usage:
solution = Solution()
print(solution.maxCoins([3, 1, 5, 8]))  # Output: 167
print(solution.maxCoins([1, 5]))        # Output: 10
