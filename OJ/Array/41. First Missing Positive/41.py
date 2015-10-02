__author__ = 'Shauro'
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Put each number in its right place.
        For example:
        When we find 5, then swap it with A[4].
        At last, the first place where its number is not right, return the place + 1.
        """
        length = len(nums)
        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1

s = Solution()
print s.firstMissingPositive([2,1])