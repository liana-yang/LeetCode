class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
    	stack = []
    	for item in path.split("/"):
        	if item not in [".", "..", ""]:
        		stack.append(item)
        	if item == ".." and stack:
        		stack.pop()
    	return "/" + "/".join(stack)




s = Solution()
print s.simplifyPath("/a/./b/../../c/")
print s.simplifyPath("/home/")
print s.simplifyPath("/../")
print s.simplifyPath("/home//foo/")