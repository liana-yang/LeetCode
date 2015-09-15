class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        for i in range(length):
        	if citations[i] >= length - i:
        		return citations[i]

s = Solution()
print s.hIndex([0,1,3,5,6])