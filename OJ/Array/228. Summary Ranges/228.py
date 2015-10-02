class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if not nums:
        	return result
        head = nums[0]
        for i in range(1, len(nums)):
        	if nums[i] != nums[i - 1] + 1:
        		if nums[i - 1] == head:
        			result.append(str(head))
        		else:
        			result.append(str(head) + '->' + str(nums[i - 1]))
        		head = nums[i]
        if nums[-1] == head:
        	result.append(str(head))
        else:
        	result.append(str(head) + '->' + str(nums[-1]))
        return result

s = Solution()
print s.summaryRanges([0,1,2,4,5,7])
print s.summaryRanges([1,3])

