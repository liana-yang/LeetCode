class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
        	if nums[lo] == nums[hi] == target:
        		return [lo, hi]
        	if nums[lo] < target:
        		lo += 1
        	if nums[hi] > target:
        		hi -= 1
        return [-1, -1]
        
s = Solution()
print s.searchRange([5, 7, 7, 8, 8, 10], 8)
