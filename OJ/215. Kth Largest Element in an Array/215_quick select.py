class Solution(object):
    def getPivot(self, nums, lo, hi):
        if lo == hi:
            return lo
        i = lo
        j = i + 1
        while j <= hi:
            if nums[j] > nums[lo]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        nums[lo], nums[i] = nums[i], nums[lo]
        return i


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) < k:
            return 0
        lo = 0
        hi = len(nums) - 1
        pivot = self.getPivot(nums, lo ,hi)
        while pivot + 1 != k:
            if pivot < k:
                lo = pivot + 1
            if pivot > k:
                hi = pivot - 1
            pivot = self.getPivot(nums, lo, hi)
        return nums[pivot]

    # The smart approach for this problem is to use the selection algorithm
    # (based on the partion method - the same one as used in quicksort).




s = Solution()
print s.findKthLargest([3,2,1,5,6,4], 2)