# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals

        result = []
        result.append(intervals[0])

        for i in range(1,len(intervals)):
            result = self.insert(result,intervals[i])

        return result

    def insert(self,intervals,newInterval):
        result = []
        for interval in intervals:
        #case 1   (...) {...}   or {...} (...)
            if interval.start > newInterval.end or interval.end < newInterval.start :
                result.append(interval)
                continue
        #case 2    ( ...{ ... } ...)
            elif interval.start <= newInterval.start and interval.end >= newInterval.end :
                return intervals
        #case 3   (..{...)...}   {...(...}...)   {...(...)...}
            else:
                newInterval.end = max(newInterval.end,interval.end)
                newInterval.start = min(newInterval.start,interval.start)
        result.append(newInterval)
        return result