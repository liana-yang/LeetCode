class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height) - 1
        result = 0
        while lo < hi:
        	result = max(result, (hi - lo) * min(height[lo], height[hi]))
        	if height[lo] < height[hi]:
        		lo += 1
        	else:
        		hi -= 1
        return result