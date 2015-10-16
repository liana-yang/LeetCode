class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        hashMap1 = {}
        hashMap2 = {}
        str = str.split()
        if len(pattern) != len(str):
        	return False
        for i in range(len(pattern)):
        	if pattern[i] not in hashMap1:
        		hashMap1[pattern[i]] = str[i]
        	elif hashMap1[pattern[i]] != str[i]:
        		return False
        for key in hashMap1:
        	if hashMap1[key] not in hashMap2:
        		hashMap2[hashMap1[key]] = key
        	elif hashMap2[hashMap1[key]] != key:
        		return False
        return True
s = Solution()
print s.wordPattern("abba", "dog cat cat dog")
print s.wordPattern("jquery", "jquery")