class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        if not n:
            return 0
        for i in range(m - n + 1): # comparision times
            j = 0
            while j < n:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == n:
                return i
        return -1

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.strStr("hello", "e")
    finish = clock()
    print (finish - start) * 1000