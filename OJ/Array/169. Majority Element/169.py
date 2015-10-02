class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        for n in nums:
        	if n not in hashMap:
        		hashMap[n] = 1
        	else:
        		hashMap[n] += 1
        for key in hashMap:
        	if hashMap[key] > len(nums) / 2:
        		return key