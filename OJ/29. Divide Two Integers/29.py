class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # determine sign of the quotient
        # positive = (dividend < 0) == (divisor < 0)
        positive = (dividend < 0) is (divisor < 0)
        # remove sign of operands
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        # test down from the highest bit
        # accumulate the tentative value for valid bits
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        # assign back the sign
        if not positive:
            res = -res
        # check for overflow and return
        return min(max(-2147483648, res), 2147483647)

        # The outer loop reduces n by at least half each iteration. 
        # So It has O(log N) iterations. 
        # The inner loop has at most log N iterations. 
        # So the overall complexity is O((log N)^2)
s = Solution()
print s.divide(16, 3)