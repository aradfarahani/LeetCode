class Solution:
    def numberOfArithmeticSlices(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        
        dp = [{} for _ in range(n)]
        total_count = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j].get(diff, 0)
                dp[i][diff] = dp[i].get(diff, 0) + count + 1
                total_count += count
        
        return total_count

# Example usage:
solution = Solution()
print(solution.numberOfArithmeticSlices([2,4,6,8,10]))  # Output: 7
print(solution.numberOfArithmeticSlices([7,7,7,7,7]))  # Output: 16
