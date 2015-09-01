class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}

    def numDistinct(self, s, t):
        m = len(t)
        n = len(s)
        if m > n:
            return 0 # impossible for subsequence
        path = [[] for i in range(m + 1)]
        # initialization
        for i in range(0, m + 1):
            if i == 0:
                for j in range(0, n + 1):
                    path[i].append(1)
            else:
                for j in range(0, n + 1):
                    path[i].append(0)
        
        for j in range(1, n + 1):
            for i in range(1, m + 1):
                path[i][j] = path[i][j - 1]
                if t[i - 1] == s[j - 1]:
                    path[i][j] += path[i - 1][j - 1]
        #print path
        return path[m][n]


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.numDistinct("rabbbit", "rabbit")
    #print s.numDistinct("AABCDEE", "ACE")
    #print s.numDistinct("aabb", "abb")
    #print s.numDistinct("aacaacca", "ca")
    finish = clock()
    print (finish - start) * 1000