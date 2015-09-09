class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        high = len(nums) - 1
        low = 0

        for i in range(low, high):
        	while nums[i] == max(nums) and i < high:
        		nums[i], nums[high] = nums[high], nums[i]
        		high -= 1
        	while nums[i] == 0 and i > low:
        		nums[i], nums[low] = nums[low], nums[i]
        		low += 1
        #return nums
s = Solution()
print s.sortColors([1,0])