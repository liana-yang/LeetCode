class Solution:
    # @param {string} s
    # @return {string}
    def isPalindromic(self, s):
        result = True
        length = len(s)
        for i in range(length / 2):
            if s[i] != s[length - 1 - i]:
                result = False
                break
        return result

    def longestPalindrome(self, s):
        longest_index = 0
        max_length = 0
        for i in range(len(s)):
            if self.isPalindromic(s[i - max_length: i + 1]):
                longest_index = i - max_length
                max_length += 1
            elif i - max_length - 1 >= 0 and self.isPalindromic(s[i - max_length - 1: i + 1]):
                longest_index = i - max_length - 1
                max_length += 2
            # print "longest_index = %s, max_length = %s" % (longest_index, max_length)

        return s[longest_index:longest_index + max_length]
        

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()   
    #print s.isPalindromic("abcb")
    print s.longestPalindrome("abacab")
    finish = clock()
    print (finish - start) * 1000