class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordFind(self, wordlist_sorted, i, word, j, length):
        
        while(j < length):
            index = word.find(wordlist_sorted[j][0])          
            if index != - 1:
                word = word[0: index] + word[index + wordlist_sorted[j][1]: len(word)]
                if word == '':
                    return True
            else:
                j += 1
        return False

    def wordBreak(self, s, wordDict):
        wordlist = {}

        for w in wordDict:
            wordlist[w] = len(w)
        wordlist_sorted = sorted(wordlist.items(), key = lambda wordlist: wordlist[1], reverse = True)

        length = len(wordlist_sorted)

        for i in range(len(wordlist_sorted)):
            word = s
            j = i
            if self.wordFind(wordlist_sorted, i, word, j, length) == True:
                return True
        return False

        

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
    finish = clock()
    print (finish - start) * 1000