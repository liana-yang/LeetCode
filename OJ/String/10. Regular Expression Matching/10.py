class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        pattern = re.compile(p)
        result = re.match(pattern, s)

        #for r in result.group():
        #    print r

        if result and result.group(0) == s:
            return True
        else:
            return False
        
if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.isMatch("aa", "aa")
    finish = clock()
    print (finish - start) * 1000