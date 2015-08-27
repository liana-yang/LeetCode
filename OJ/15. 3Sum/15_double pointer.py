class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums) - 1):
        	if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
        	    lo = i + 1
        	    hi = len(nums) - 1
        	    sum = 0 - nums[i]
        	    while lo < hi:
        			if nums[lo] + nums[hi] == sum:
        				result.append([nums[i], nums[lo], nums[hi]])
        				while lo < hi and nums[lo] == nums[lo + 1]:
        					lo += 1
        				while lo < hi and nums[hi] == nums[hi - 1]:
        					hi -= 1
        				lo += 1
        				hi -= 1
        			elif nums[lo] + nums[hi] < sum:
        				lo += 1
        			else:
        				hi -= 1
        return result



if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.threeSum([-1,0,1,2,-1,-4])
    finish = clock()
    print (finish - start) * 1000