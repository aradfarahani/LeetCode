class Solution:
    def isSelfCrossing(self, distance):
        for i in range(3, len(distance)):
            # Case 1: Current line crosses the line 3 steps back
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True
            # Case 2: Current line crosses the line 4 steps back
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True
            # Case 3: Current line crosses the line 5 steps back
            if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i] + distance[i - 4] >= distance[i - 2] and distance[i - 1] <= distance[i - 3] and distance[i - 1] + distance[i - 5] >= distance[i - 3]:
                return True
        return False

# Example usage:
solution = Solution()
print(solution.isSelfCrossing([2, 1, 1, 2]))  # Output: True
print(solution.isSelfCrossing([1, 2, 3, 4]))  # Output: False
print(solution.isSelfCrossing([1, 1, 1, 2, 1]))  # Output: True
