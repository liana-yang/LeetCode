class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
        	return 0
        INT_MAX = 2147483647
        low, high = 1, INT_MAX
        while True:
        	mid = low + (high - low) / 2
        	if mid > x / mid:
        		high = mid - 1
        	else:
        		if mid + 1 > x / (mid + 1):
        			return mid
        		low = mid + 1

s = Solution()
print s.mySqrt(9)
        