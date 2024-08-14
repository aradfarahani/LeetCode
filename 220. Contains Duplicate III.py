from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        sorted_list = SortedList()
        
        for i in range(len(nums)):
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])
            
            pos1 = SortedList.bisect_left(sorted_list, nums[i] - valueDiff)
            pos2 = SortedList.bisect_right(sorted_list, nums[i] + valueDiff)
            
            if pos1 != pos2 and pos1 != len(sorted_list):
                return True
            
            sorted_list.add(nums[i])
        
        return False

# Example usage:
solution = Solution()
print(solution.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0))  # Output: True
print(solution.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))  # Output: False
