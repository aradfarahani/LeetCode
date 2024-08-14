from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        def maxSumSubarray(arr, k):
            sorted_list = SortedList([0])
            cur_sum, max_sum = 0, float('-inf')
            for num in arr:
                cur_sum += num
                idx = sorted_list.bisect_left(cur_sum - k)
                if idx < len(sorted_list):
                    max_sum = max(max_sum, cur_sum - sorted_list[idx])
                sorted_list.add(cur_sum)
            return max_sum
        
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        
        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                for r in range(rows):
                    row_sums[r] += matrix[r][right]
                max_sum = max(max_sum, maxSumSubarray(row_sums, k))
        
        return max_sum

# Example usage:
solution = Solution()
print(solution.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))  # Output: 2
print(solution.maxSumSubmatrix([[2,2,-1]], 3))  # Output: 3
