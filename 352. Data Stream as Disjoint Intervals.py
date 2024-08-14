from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()

    def addNum(self, value: int) -> None:
        if value in self.intervals:
            return
        
        keys = self.intervals.keys()
        l = self.intervals.bisect_left(value)
        r = self.intervals.bisect_right(value)
        
        left_merge = (l > 0 and self.intervals[keys[l - 1]][1] + 1 >= value)
        right_merge = (r < len(self.intervals) and keys[r] == value + 1)
        
        if left_merge and right_merge:
            left = keys[l - 1]
            right = keys[r]
            self.intervals[left] = (self.intervals[left][0], self.intervals[right][1])
            del self.intervals[right]
        elif left_merge:
            left = keys[l - 1]
            self.intervals[left] = (self.intervals[left][0], max(self.intervals[left][1], value))
        elif right_merge:
            right = keys[r]
            self.intervals[value] = (value, self.intervals[right][1])
            del self.intervals[right]
        else:
            self.intervals[value] = (value, value)

    def getIntervals(self) -> list:
        return list(self.intervals.values())

# Example usage:
summaryRanges = SummaryRanges()
summaryRanges.addNum(1)
print(summaryRanges.getIntervals())  # Output: [[1, 1]]
summaryRanges.addNum(3)
print(summaryRanges.getIntervals())  # Output: [[1, 1], [3, 3]]
summaryRanges.addNum(7)
print(summaryRanges.getIntervals())  # Output: [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2)
print(summaryRanges.getIntervals())  # Output: [[1, 3], [7, 7]]
summaryRanges.addNum(6)
print(summaryRanges.getIntervals())  # Output: [[1, 3], [6, 7]]
