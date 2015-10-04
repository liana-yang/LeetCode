class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
        	if nums[lo + 1] > nums[lo]:
        		lo += 1
        	else:
        		return nums[lo + 1]
        return nums[0]
        
s = Solution()
print s.findMin([4,5,6,7,0,1,2])
print s.findMin([1,2])
