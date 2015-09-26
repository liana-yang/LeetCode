class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
        	return False
        low = 0
        high = len(nums) - 1
        while low <= high:
        	mid = low + (high - low) / 2
        	if target == nums[mid]:
        		return True
        	# tricky part
        	while low < mid and nums[low] == nums[mid]:
        		low += 1
        	# the first half is ordered
        	if nums[low] <= nums[mid]:
        		# target is in the first half
        		if nums[low] <= target <= nums[mid]:
        			high = mid - 1
        		else:
        			low = mid + 1
        	# the second half is ordered
        	else:
        		# target is in the second half
        		if nums[mid] <= target <= nums[high]:
        			low = mid + 1
        		else:
        			high = mid - 1
        return False