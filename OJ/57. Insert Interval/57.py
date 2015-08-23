# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(Interval(start, end))
        result += intervals[i:]
        for v in result:
            print v.start
            print v.end
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()
    m1 = Interval(1, 4)
    m2 = Interval(10, 12)
    m3 = Interval(5, 13)
    m4 = Interval(13, 14)
    #m5 = Interval(9, 11)
    #m1 = Interval(1, 5)
    #m3 = Interval(0, 1)
    Intervals = []
    Intervals.append(m1) 
    Intervals.append(m2)
    Intervals.append(m4)
    #Intervals.append(m5)  
    s.insert(Intervals, m3)     
    #s.insert([[1,3],[6,9]], [2,5])
    #s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,9])
    finish = clock()
    print (finish - start) * 1000