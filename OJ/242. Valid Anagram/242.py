class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for c in s:
        	if c not in hashMap:
	        	hashMap[c] = 1
	        else:
	        	hashMap[c] += 1
        for c in t:
        	if c not in hashMap:
        		return False
        	else:
        		hashMap[c] -= 1
        		# if hashMap[c] < 0:
        			# return False
        for key in hashMap:
        	if hashMap[key] != 0:
        		return False
        return True
s = Solution()
print s.isAnagram("anagram", "nagaram")