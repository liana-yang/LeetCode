class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # compare half of the digits in x, so don't need to deal with overflow.
        if x < 0 or (x != 0 and x % 10 == 0):
        	return False
        rev = 0
        while x > rev:
        	rev = rev * 10 + x % 10;
        	x = x / 10
        return x == rev or x == rev / 10