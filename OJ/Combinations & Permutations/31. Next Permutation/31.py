class Solution(object):
    def reverse(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)- 1
        while i > 0 and nums[i - 1] >= nums[i]:
        	i -= 1
        if i == 0:   # nums are in descending order
        	self.reverse(nums, 0, len(nums) - 1)
        	return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
        	j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        """
        l, r = k + 1, len(nums) - 1  # reverse the second part
        while l < r:
        	nums[l], nums[r] = nums[r], nums[l]
        	l += 1 ; r -= 1
        """
        self.reverse(nums, k + 1, len(nums) - 1)
        
        print nums

        """
        Find the largest index i such that nums[i] < nums[i + 1]. 
        If no such index exists, the permutation is sorted in descending order, 
        just reverse it to ascending order and we are done. 
        For example, the next permutation of [3, 2, 1] is [1, 2, 3].

        Find the largest index k greater than j such that nums[j] <= nums[k].
        Swap the value of nums[j] with that of nums[k].
        Reverse the sequence from nums[k + 1] up to and including the final element nums[len(nums) - 1].
        """

s = Solution()
s.nextPermutation([1,3,4,2])