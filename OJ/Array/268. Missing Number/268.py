class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use bit manipulation
        result = len(nums)
        i = 0
        for n in nums:
        	result ^= n
        	result ^= i
        	i += 1
        return result


s = Solution()
print s.missingNumber([1,2,0,5,3])
print s.missingNumber([3,2,0])