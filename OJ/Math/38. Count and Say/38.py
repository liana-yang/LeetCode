class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        temp = ''
        for i in range(1, n):
        	temp = result
        	result = ''
        	count = 1
        	say = temp[0]
        	for j in range(1, len(temp)):
        		if temp[j] != say:
        			result += str(count) + say
        			count = 1
        			say = temp[j]
        		else:
        			count += 1
        	result += str(count) + say
        return result

s = Solution()
print s.countAndSay(5)