# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        length = len(intervals)
        i = length - 1
        appended = False
        key1 = - 1
        key2 = - 1
        if length == 0:
            intervals.append([newInterval.start, newInterval.end])
            appended = True
        while(i >= 0):
            existed = True
            inserted = False
            if appended == False:
                if newInterval.start < intervals[i].start:
                    if (i == 0 and intervals[i].start <= newInterval.end) or (i != 0 and newInterval.start > intervals[i - 1].end and intervals[i].start <= newInterval.end):
                        intervals[i].start = newInterval.start
                        if key1 > - 1:
                            intervals[i].end = newInterval.end
                            del intervals[key1]
                    elif (i == 0 or (newInterval.start > intervals[i - 1].end and intervals[i].start > newInterval.end)) and intervals[i].start > newInterval.end:
                        intervals.insert(i, [newInterval.start, newInterval.end])
                        appended = True
                        inserted = True
                    if inserted == False:
                        if newInterval.end > intervals[i].end and i != length - 1:
                            del intervals[i]
                            key1 -= 1
                            key2 -= 1
                            existed = False
                            if key1 <= - 1:
                                if i == 0 or (intervals[i - 1].end < newInterval.start and intervals[i].start <= newInterval.end):
                                    intervals[i].start = newInterval.start
            if inserted == False and appended == False:
                if existed == True:
                    if newInterval.end > intervals[i].end:
                        if (i == length - 1 and intervals[i].end >= newInterval.start) or (i != length - 1 and newInterval.end < intervals[i + 1].start):
                            intervals[i].end = newInterval.end
                            key1 = i
                        elif i == length - 1 and intervals[i].end < newInterval.start:
                            intervals.append([newInterval.start, newInterval.end])
                            appended = True
                elif intervals[i - 1].end < newInterval.start and newInterval.end < intervals[i].start:
                    intervals.insert(i, [newInterval.start, newInterval.end])
                    inserted == True
                    appended == True
                    break
            if len(intervals) > 1 and existed == True and appended == False and inserted == False:
                #print "key2 = %s" % key2
                if key2 <= - 1: 
                    if intervals[i].start <= newInterval.end <= intervals[i].end:
                        key2 = i
                elif intervals[i].start <= newInterval.start <= intervals[i].end:
                    intervals[i].end = intervals[key2].end
                    del intervals[key2]
                    break

            i -= 1

        #length = len(intervals)
        #i = length - 1
        #while(i > 0):
            #if appended == False:
                #if intervals[i].start == newInterval.end and intervals[i - 1].end == newInterval.start:
                    #intervals[i].start = intervals[i - 1].start
                    #del intervals[i - 1]
                    #break 
                
        for v in intervals:
            print v.start
            print v.end
        return intervals


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