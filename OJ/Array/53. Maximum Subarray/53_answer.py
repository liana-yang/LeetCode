class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        print list(set(nums))

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()
    s.removeDuplicates([1,1,2])
    finish = clock()
    print (finish - start) * 1000