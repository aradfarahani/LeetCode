class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        
        return nums[left]

# Example usage:
solution = Solution()
print(solution.findMin([1, 3, 5]))  # Output: 1
print(solution.findMin([2, 2, 2, 0, 1]))  # Output: 0
