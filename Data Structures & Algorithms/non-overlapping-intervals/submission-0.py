class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x : x[0])
        lastValue = intervals[0][1]
        res = 0
        for start, end in intervals[1:]:
            if start >= lastValue:
                lastValue = end
            else:
                res += 1
                lastValue = min(lastValue, end)
        return res