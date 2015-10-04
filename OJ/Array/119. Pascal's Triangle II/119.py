class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        stack = []
        for i in range(rowIndex + 1):
        	if i == 0:
        		stack.append(1)
        	elif i == 1:
        		stack.append(1)
        	else:
        		j = i - 1
        		while j > 0:
        			stack[j] += stack[j - 1]
        			j -= 1
        		stack.append(1)
        return stack

s = Solution()
print s.getRow(3)