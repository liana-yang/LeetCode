class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(nums)):
        	if nums[i] not in hashMap:
        		hashMap[nums[i]] = i
        	elif hashMap[nums[i]] < i - k:
        		hashMap[nums[i]] = i
        	else:
        		return True
        return False