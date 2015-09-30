class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.longestConsecutive([100, 4, 200, 1, 3, 2])
    print s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])
    print s.longestConsecutive([0,0])
    finish = clock()
    print (finish - start) * 1000