class Solution:
    def countRangeSum(self, nums, lower, upper):
        def merge_sort(sums, lower, upper):
            if len(sums) <= 1:
                return 0
            mid = len(sums) // 2
            left = sums[:mid]
            right = sums[mid:]
            count = merge_sort(left, lower, upper) + merge_sort(right, lower, upper)
            i = j = k = 0
            while i < len(left):
                while j < len(right) and right[j] - left[i] < lower:
                    j += 1
                while k < len(right) and right[k] - left[i] <= upper:
                    k += 1
                count += k - j
                i += 1
            sums[:] = sorted(left + right)
            return count
        
        prefix_sums = [0]
        for num in nums:
            prefix_sums.append(prefix_sums[-1] + num)
        
        return merge_sort(prefix_sums, lower, upper)

# Example usage:
solution = Solution()
print(solution.countRangeSum([-2, 5, -1], -2, 2))  # Output: 3
print(solution.countRangeSum([0], 0, 0))           # Output: 1
