class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for i in range(1, 4):
        	if s[0: i] and int(s[0: i]) < 256 and (i == 1 or s[0] != '0'):
        		for j in range(i + 1, i + 4):
        			if s[i: j] and int(s[i: j]) < 256 and (j - i == 1 or s[i] != '0'):
        				for k in range(j + 1, j + 4):
        					if s[j: k] and int(s[j: k]) < 256 and (k - j == 1 or s[j] != '0'):
        						if s[k:] and int(s[k:]) < 256 and (len(s) - k == 1 or s[k] != '0'):
        							result.append(s[0: i] + '.' + s[i: j] + '.' + s[j: k] + '.' + s[k:])
        return result
s = Solution()
print s.restoreIpAddresses("25525511135")
print s.restoreIpAddresses("010010")