"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        print(intervals)
        for i in range(len(intervals) - 1):
            start, end = intervals[i].start, intervals[i].end
            print(f'Current start: {start}, end:{end}')
            nextStart, nextEnd = intervals[i+1].start, intervals[i+1].end
            print(f'Next start: {nextStart}, end:{nextEnd}')

            if end > nextStart:
                return False
        return True

