class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        pos = len(result) - 1
        for n1 in reversed(num1):
        	tempPos = pos
        	for n2 in reversed(num2):
        		result[tempPos] += int(n1) * int(n2)
        		result[tempPos - 1] += result[tempPos] / 10
        		result[tempPos] %= 10
        		tempPos -= 1
        	pos -= 1
        pt = 0
        while pt < len(result) - 1 and result[pt] == 0: 
        # take care of the case if 'n' * '0', use pt < len(result) - 1, not pt < len(result)
        	pt += 1
        return ''.join(map(str, result[pt:]))

s = Solution()
print s.multiply('1','1')
