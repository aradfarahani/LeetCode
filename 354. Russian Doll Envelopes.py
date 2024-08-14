from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        # Sort envelopes by width in ascending order and by height in descending order if widths are the same
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract the heights
        heights = [envelope[1] for envelope in envelopes]
        
        # Find the LIS based on heights
        lis = []
        for height in heights:
            pos = bisect_left(lis, height)
            if pos == len(lis):
                lis.append(height)
            else:
                lis[pos] = height
        
        return len(lis)

# Example usage:
solution = Solution()
print(solution.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))  # Output: 3
print(solution.maxEnvelopes([[1,1],[1,1],[1,1]]))  # Output: 1
