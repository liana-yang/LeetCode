class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        n = 1
        while length > 0 and s[length - 1] == ' ':
        	length -= 1
        while n <= length:
        	if s[length - n] == ' ':
        		return n - 1
        	n += 1
        return length

s = Solution()
print s.lengthOfLastWord("Hello World")
print s.lengthOfLastWord("        ")
print s.lengthOfLastWord("a ")