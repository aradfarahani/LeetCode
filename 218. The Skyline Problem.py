import heapq

class Solution:
    def getSkyline(self, buildings):
        # Create a list of all events
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        
        # Sort events by x-coordinate, and by height in case of ties
        events.sort()
        
        # Result list and a max-heap to keep track of the current buildings
        result = [[0, 0]]
        heap = [(0, float('inf'))]
        
        for x, negH, R in events:
            # Remove the buildings from the heap that are already passed
            while heap[0][1] <= x:
                heapq.heappop(heap)
            
            # If it's the start of a building, add it to the heap
            if negH != 0:
                heapq.heappush(heap, (negH, R))
            
            # If the current highest building has changed, add the point to the result
            if result[-1][1] != -heap[0][0]:
                result.append([x, -heap[0][0]])
        
        return result[1:]

# Example usage:
solution = Solution()
print(solution.getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))  # Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
print(solution.getSkyline([[0, 2, 3], [2, 5, 3]]))  # Output: [[0,3],[5,0]]
