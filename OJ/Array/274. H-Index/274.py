class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
        	return 0
        length = len(citations)
        h = 0
        count = [0 for i in range(length + 1)]
        for c in citations:
        	count[min(c, length)] += 1
        for i in range(length + 1):
        	h += count[length - i]
        	if h >= length - i:
        		return length - i

s = Solution()
print s.hIndex([3, 0, 6, 1, 5])