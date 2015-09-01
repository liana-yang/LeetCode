class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}

    def numDistinct(self, s, t):
        m = len(t)
        n = len(s)
        if m > n:
            return 0
        path = [0 for i in range(m + 1)]
        path[0] = 1
        for j in range(1, n + 1):
            # traversing backwards so we are using path[i-1] from last time step
            i = m
            while i >= 1:
                if t[i - 1] == s[j - 1]:
                    path[i] += path[i - 1]
                i -= 1
        return path[m]



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