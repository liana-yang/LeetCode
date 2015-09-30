class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        reach = 0
        while i < len(nums) and i <= reach:
        	reach = max(i + nums[i], reach)
        	i += 1
        return i == len(nums)

s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])