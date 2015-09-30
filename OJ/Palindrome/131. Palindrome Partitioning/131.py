class Solution:
    # @param {string} s
    # @return {string[][]}
    def isPalindromic(self, s):
        result = True
        length = len(s)
        for i in range(length / 2):
            if s[i] != s[length - 1 - i]:
                result = False
                break
        return result

    def backTracking(self, s, result, stack):     
        for i in range(0, len(s) + 1):
            if i == 0:
                continue
            if self.isPalindromic(s[0: i]):
                #print s
                #print i
                stack.append(s[0: i])
                if i != len(s):
                    new_s = s[i: len(s)]
                    self.backTracking(new_s, result, stack)
                else:
                    result.append(stack[:])
                    #print "s = %s, i = %s" % (s, i)
                    #print stack
                    if stack:
                        stack.pop()
        if stack:
            stack.pop()
        return result

    def partition(self, s):
        result = []
        stack = []
        return self.backTracking(s, result, stack)


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.partition("aaaa")
    print s.partition("bb")
    finish = clock()
    print (finish - start) * 1000