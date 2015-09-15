class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        hasZero = False
        allZero = True
        for n in nums:
        	if n == 0 and not hasZero:
        		hasZero = True
        	else:
        		total *= n
        		allZero = False
        		
        if allZero:
        	return [0 for n in nums]
        result = []
        for n in nums:
        	if hasZero:
        		if n != 0:
        			result.append(0)
        		else:
        			result.append(total)
        	else:
        		result.append(total / n)
        return result

s = Solution()
print s.productExceptSelf([0,4,0])