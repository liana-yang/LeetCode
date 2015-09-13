class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # Since the given array contains only positive integers, 
        # the subarray sum can only increase by including more elements. 
        # Therefore, you don't have to include more elements 
        # once the current subarray already has a sum large enough. 
        # This gives the linear time complexity solution 
        # by maintaining a minimum window with a two indices.
        firstPos = 0
        numberSum = 0
        INT_MAX = 2147483647
        minLength = INT_MAX
        for i in range(len(nums)):
        	numberSum += nums[i]
        	while numberSum >= s:
        		minLength = min(minLength, i - firstPos + 1)
        		numberSum -= nums[firstPos]
        		firstPos += 1
        if minLength == INT_MAX:
        	return 0
        else:
        	return minLength

s = Solution()
print s.minSubArrayLen(7, [2,3,1,2,4,3])