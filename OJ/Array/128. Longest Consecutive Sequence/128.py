class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        result = 0
        length = 0
        nums.sort()
        #print nums
        for i in range(len(nums)):
            if i == 0:
                length += 1
                if len(nums) == 1:
                    return 1
            else:
                gap = nums[i] - nums[i - 1]
                if gap == 1:
                    length += 1
                if gap > 1 or i == len(nums) - 1:
                    if length > result:
                        result = length
                    length = 1
            #print "i = %s, length = %s" % (i, length)
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
    print s.longestConsecutive([0,0])
    finish = clock()
    print (finish - start) * 1000