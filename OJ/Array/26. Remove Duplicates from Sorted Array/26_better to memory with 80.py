class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        newTail = 0
        for n in nums:
            if n != nums[newTail]:
                nums[newTail + 1] = n
                newTail += 1
        return newTail + 1