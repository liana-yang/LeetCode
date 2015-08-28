class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        newTail = 0
        for n in nums:
            if newTail < 2 or n > nums[newTail - 2]:
                nums[newTail] = n
                newTail += 1
        return newTail

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()
    print s.removeDuplicates([1,1,1,2,2,3])
    finish = clock()
    print (finish - start) * 1000