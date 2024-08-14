from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        
        result = []
        deq = deque()
        
        for i in range(len(nums)):
            # Remove elements not within the sliding window
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove elements smaller than the current element from the deque
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # Add the current element's index to the deque
            deq.append(i)
            
            # Append the maximum element of the current window to the result
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result

# Example usage:
solution = Solution()
print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # Output: [3, 3, 5, 5, 6, 7]
print(solution.maxSlidingWindow([1], 1))  # Output: [1]
