class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
        	return ''
        result = '1'
        temp = ''
        for i in range(1, n): # run from starting to generate second string
        	length = len(result)
        	for j in range(0, length):
        		count = 1 # we have at least 1 occourence of each digit
        		# get the number of times same digit occurred (be carefull with the end of the string)
        		while j < length - 1 and result[j] == result[j + 1]:
        			count += 1
        			j += 1 # we need to keep increasing the index inside of the stringb
        		temp += str(count) + result[j] # add to new string "count"+"digit itself"
        		if j == length - 1:
        			break
           	result = temp # save temporary result
        	temp = '' # clean our string-helper
        return result

s = Solution()
print s.countAndSay(5)