class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            if nums[lo] < nums[hi]:
                return nums[lo]
            mid = lo + (hi - lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else: # when num[mid] and num[hi] are same
            	hi -= 1
        return nums[lo]

        """
        When num[mid] == num[hi], 
        we couldn't sure the position of minimum in mid's left or right, 
        so just let upper bound reduce one.
        """

s = Solution()
print s.findMin([4,5,6,7,0,0,1,1,2])
print s.findMin([1,2,2])
print s.findMin([2,2,2,1,1,0,0])