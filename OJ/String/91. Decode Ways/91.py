class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
        	return 0
        r1 = 1 # r1 decode ways of s[i - 1], empty string originally
        r2 = 1 # r2 decode ways of s[i - 2], single string originally
        for i in range(1, len(s)):
        	if s[i] == '0':
        		r1 = 0
        	if s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
        		r1 = r1 + r2
        		r2 = r1 - r2 # r2 = r1 (old)
        	else:
        		r2 = r1
        return r1 