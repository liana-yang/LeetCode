class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if not nums:
            return result
        length = len(nums)
        i = 0
        while i < length:
            start = i
            end = i
            while end < length - 1 and nums[end + 1] == nums[end] + 1:
                end += 1
            if end > start:
                result.append(str(nums[start]) + '->' + str(nums[end]))
            else:
                result.append(str(nums[start]))
            i = end + 1
        return result


s = Solution()
print s.summaryRanges([0,1,2,4,5,7])
print s.summaryRanges([1,3])