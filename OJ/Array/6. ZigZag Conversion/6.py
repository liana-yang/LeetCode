class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        result = ''
        if numRows == 1:
        	return s
        for i in range(0, numRows):
        	step1 = (numRows - i - 1) * 2
        	step2 = i * 2
        	pos = i
        	if pos < length:
        		result += s[pos]
        	while True:
        		pos += step1
        		if pos >= length:
        			break
        		if step1 > 0:
        			result += s[pos]
        		pos += step2
        		if pos >= length:
        			break
        		if step2 > 0:
        			result += s[pos]
        return result




s = Solution()
print s.convert("PAYPALISHIRING", 3)
        