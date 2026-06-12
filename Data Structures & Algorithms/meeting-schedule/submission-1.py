"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x[0])
        lastValue = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= lastValue:
                lastValue = end
                continue
            return False
        return True
            