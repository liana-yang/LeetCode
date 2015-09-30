class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        dp = [0 for i in range(length)]
        for i in range(0, length - 1):
        	for j in range(nums[i]):
        		if i + 1 + j < length:
        			dp[i + 1 + j] += 1
        if dp[-1] > 0:
        	return True
        else:
        	return False

s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])