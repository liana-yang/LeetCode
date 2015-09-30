class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
        	if nums[lo] == val:
        		nums[lo] = nums[hi]
        		nums[hi] = val
        		hi -= 1
        	else:
        		lo += 1
        return lo
        

s = Solution()
print s.removeElement([1,2,3,2,4], 2)