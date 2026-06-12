"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0    
        intervals.sort(key = lambda x : x.start)
        days = 1
        lastValue = intervals[0].end
        for target in intervals[1:]:
            if target.start >= lastValue:
                lastValue = target.end
                continue
            days += 1
            lastValue = min(lastValue, target.end)
        return days