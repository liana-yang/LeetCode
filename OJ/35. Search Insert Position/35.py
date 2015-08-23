class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        length = len(nums)
        for i in range(length):
            if target <= nums[i]:
                return i
        return length

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.searchInsert([1,3,5,6], 5)
    print s.searchInsert([1,3,5,6], 2)
    print s.searchInsert([1,3,5,6], 7)
    print s.searchInsert([1,3,5,6], 0)
    finish = clock()
    print (finish - start) * 1000