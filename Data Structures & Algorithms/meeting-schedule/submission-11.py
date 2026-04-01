"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x : x.start)
        prevValue = intervals[0].end
        for target in intervals[1:]:
            if target.start >= prevValue:
                prevValue = target.end
                continue
            return False
        return True
            