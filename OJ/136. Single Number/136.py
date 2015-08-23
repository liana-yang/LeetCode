class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        if nums:
            result = nums[0]
            for i in range(1, len(nums)):
                result ^= nums[i]
            return result
        else:
            return 0


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.singleNumber([1,1,2,2,3])
    finish = clock()
    print (finish - start) * 1000