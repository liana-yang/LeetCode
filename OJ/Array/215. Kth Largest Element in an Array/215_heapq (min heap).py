import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in nums:
            heapq.heappush(heap, - i)
        for i in range(k):
            res = - heapq.heappop(heap)
        return res



s = Solution()
print s.findKthLargest([3,2,1,5,6,4], 2)