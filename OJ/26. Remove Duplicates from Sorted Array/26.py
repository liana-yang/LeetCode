class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        length = len(nums)
        i = length
        while(i > 1):
            if nums[i - 2] == nums[i - 1]:
                del nums[i - 2]
                length -= 1
            i -= 1 

        print nums
        print "length = %s" % length
        return length

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()
    s.removeDuplicates([1,1,2,3,3])
    finish = clock()
    print (finish - start) * 1000