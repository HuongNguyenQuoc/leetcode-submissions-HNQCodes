"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : x.start)
        lastValue = intervals[0].end
        for target in intervals[1:]:
            if target.start >= lastValue:
                lastValue = target.end
                continue
            return False
        return True
            