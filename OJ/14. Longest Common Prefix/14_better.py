class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        pre = strs[0]
        i = 1
        while i < len(strs):
            while strs[i].find(pre) != 0:
                pre = pre[0: len(pre) - 1]
            i += 1
        return pre

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.longestCommonPrefix(["longman", "longday", "longlong"])
    print s.longestCommonPrefix(["aa","a"])
    finish = clock()
    print (finish - start) * 1000