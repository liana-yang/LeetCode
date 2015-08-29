class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        f = [False for i in range(0, len(s) + 1)]
        f[0] = True
        for i in range(1, len(s) + 1):
            #for j in range(0, i):
            j = i - 1
            while j >= 0:
                if f[j] and s[j: i] in wordDict:
                    f[i] = True
                    break
                j -= 1
        return f[len(s)]

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()   
    #print s.wordBreak("leetcode", ["leet", "code"])
    #print s.wordBreak("leetcode", ["meow", "leet"])
    #print s.wordBreak("aaaaaaa", ["aaaa","aaa"])
    print s.wordBreak("abcd", ["a","abc","b","cd"])
    print s.wordBreak("a", [])
    finish = clock()
    print (finish - start) * 1000