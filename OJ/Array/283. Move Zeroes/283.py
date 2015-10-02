class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start = 0
        end = 0
        while end < len(nums) - 1:
        	if nums[end] == 0:
        		if nums[end + 1] != 0:
        			temp = start
        			nums[start], nums[end + 1] = nums[end + 1], nums[start]
        			start = temp + 1
        	else:
        		start += 1
        	end += 1

s = Solution()
print s.moveZeroes([0,1,2,0,0,4,0,5,6])
print s.moveZeroes([0,1,2,3,0,4,0,5,6])