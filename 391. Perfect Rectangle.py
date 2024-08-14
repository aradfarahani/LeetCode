from collections import defaultdict

class Solution:
    def isRectangleCover(self, rectangles):
        def add_point(point):
            if point in points:
                points.remove(point)
            else:
                points.add(point)
        
        points = set()
        area = 0
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            
            add_point((x1, y1))
            add_point((x1, y2))
            add_point((x2, y1))
            add_point((x2, y2))
        
        if (min_x, min_y) not in points or (min_x, max_y) not in points or (max_x, min_y) not in points or (max_x, max_y) not in points or len(points) != 4:
            return False
        
        return area == (max_x - min_x) * (max_y - min_y)

# Example usage:
solution = Solution()
print(solution.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))  # Output: True
print(solution.isRectangleCover([[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]))  # Output: False
print(solution.isRectangleCover([[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]))  # Output: False
