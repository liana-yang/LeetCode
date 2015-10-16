class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hashMap = {}
        result = []
        i = 0
        for i in range(len(s) - 9):
        	s1 = s[i: i + 10]
        	if s1 not in hashMap:
        		hashMap[s1] = 1
        	elif hashMap[s1] == 1:
        		hashMap[s1] = 0
        		result.append(s1)
        return result

s = Solution()
# print s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print s.findRepeatedDnaSequences("AAAAAAAAAAA")