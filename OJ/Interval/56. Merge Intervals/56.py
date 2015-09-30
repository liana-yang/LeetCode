# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def iteration(self, intervals):
        result = []
        i = 0
        while i < len(intervals):
            start = intervals[i].start
            end = intervals[i].end
            if i != len(intervals) - 1 and end >= intervals[i + 1].start:
                if start <= intervals[i + 1].end:
                    start = min(start, intervals[i + 1].start)
                    end = max(end, intervals[i + 1].end)
                else:
                    temp1 = intervals[i + 1].start
                    temp2 = intervals[i + 1].end
                    result.append(Interval(temp1, temp2))
                intervals[i + 1].start = start
                intervals[i + 1].end = end
            else:
                result.append(intervals[i])
            i += 1
        return result

    def merge(self, intervals):
        temp = intervals
        result = []
        while result != temp:
            result = self.iteration(temp)
            temp = self.iteration(result)
        
        #for v in result:
            #print "[%s, %s]" % (v.start, v.end)
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    m1 = Interval(1, 4)
    m2 = Interval(0, 0)
    m3 = Interval(8, 10)
    m4 = Interval(15, 18)
    Intervals = []
    Intervals.append(m1) 
    Intervals.append(m2)
    #Intervals.append(m3)
    #Intervals.append(m4)
    s.merge(Intervals)
    finish = clock()
    print (finish - start) * 1000