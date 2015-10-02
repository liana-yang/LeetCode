class Solution(object):
    def reverse(self, nums, start, end):
	    while start < end:
	    	temp = nums[start]
	    	nums[start] = nums[end]
	    	nums[end] = temp
	    	start += 1
	    	end -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        self.reverse(nums, 0, length - 1)
        self.reverse(nums, 0, k - 1)
        self. reverse(nums, k ,length - 1)


s = Solution()
print s.rotate([1,2,3,4,5,6,7],3)
#print s.rotate([1,2],1)
print s.rotate([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],38)