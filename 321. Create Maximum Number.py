class Solution:
    def maxNumber(self, nums1, nums2, k):
        def maxArray(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]
        
        def merge(nums1, nums2):
            return [max(nums1, nums2).pop(0) for _ in range(len(nums1) + len(nums2))]
        
        max_num = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            max_num = max(max_num, merge(maxArray(nums1, i), maxArray(nums2, k - i)))
        return max_num

# Example usage:
solution = Solution()
print(solution.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))  # Output: [9, 8, 6, 5, 3]
print(solution.maxNumber([6, 7], [6, 0, 4], 5))  # Output: [6, 7, 6, 0, 4]
print(solution.maxNumber([3, 9], [8, 9], 3))  # Output: [9, 8, 9]
