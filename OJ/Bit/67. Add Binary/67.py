class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        result = ''
        temp = 0
        while (i >= 0 or j >= 0 or temp == 1):
        	if i >= 0:
        		temp += int(a[i])
        		i -= 1
        	if j >= 0:
        		temp += int(b[j])
        		j -= 1
        	result = str(temp % 2) + result
        	temp /= 2 # add 0 or 1 to the higher bit
        return result


s = Solution()
print s.addBinary('11', '1')