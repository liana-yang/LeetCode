class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        increment = 1
        while i >= 0:
        	temp = digits[i] + increment
        	digits[i] = temp % 10
        	increment = temp / 10
        	i -= 1
        if increment == 1:
        	digits.insert(0, 1)
        return digits



s = Solution()
print s.plusOne([1,2,3])
print s.plusOne([9,9,9])