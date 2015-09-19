class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if not s:
        	return result
        k = len(words[0])
        hashMap = {}
        total = len(words)
        for i in range(len(s)):
        	for w in words:
        		hashMap[w] = 1
        	pos = i
        	count = 0
        	while pos < len(s):
        		if count == total:
        			result.append(pos - count * k)
        			break
        		temp = s[pos: pos + k]
        		if temp in hashMap and hashMap[temp] == 1:
        			hashMap[temp] = 0
        			count += 1
        			pos += k
        		else:
        			break
        return result


s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo", "bar"])