class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}

    def numDistinct(self, s, t):
        result = 0
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.numDistinct("rabbbit", "rabbit")
    #print s.numDistinct("AABCDEE", "ACE")
    #print s.numDistinct("aabb", "abb")
    print s.numDistinct("aacaacca", "ca")
    finish = clock()
    print (finish - start) * 1000