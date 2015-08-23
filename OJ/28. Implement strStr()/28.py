class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        return haystack.find(needle)

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.strStr("hello", "e")
    finish = clock()
    print (finish - start) * 1000