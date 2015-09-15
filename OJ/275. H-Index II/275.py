class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        lo = 0
        hi = length - 1
        while lo <= hi:
        	mid = (lo + hi) / 2
        	if citations[mid] == length - mid:
        		return citations[mid]
        	#if citations[mid] < length - mid:
        	elif citations[mid] < length - mid:
        		lo = mid + 1
        	else:
        		hi = mid - 1
        #return length - lo
        return length - (hi + 1)
        # Just binary search, each time check citations[mid] 
        # case 1: citations[mid] == len-mid, 
        # then it means there are citations[mid] papers that have at least citations[mid] citations. 
        # case 2: citations[mid] > len-mid, 
        # then it means there are citations[mid] papers that have more than citations[mid] citations, 
        # so we should continue searching in the left half 
        # case 3: citations[mid] < len-mid, 
        # we should continue searching in the right side After iteration, 
        # it is guaranteed that right+1 is the one we need to find 
        # (i.e. len-(right+1) papars have at least lenth-(righ+1) citations)

s = Solution()
print s.hIndex([0,1,3,5,6])