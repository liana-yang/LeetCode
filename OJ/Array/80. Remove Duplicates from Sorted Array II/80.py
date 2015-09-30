class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        length = len(nums)
        i = length
        count = 1
        while(i > 1):
            if nums[i - 2] == nums[i - 1]:
                count += 1
                if count > 2:
                    del nums[i - 2]
                    count -= 1
                    length -= 1
            else:
                count = 1
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
    s.removeDuplicates([1,1,1,2,2,3])
    finish = clock()
    print (finish - start) * 1000