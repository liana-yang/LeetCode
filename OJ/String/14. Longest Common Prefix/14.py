class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        result = ''
        if strs:
            temp = []
            for s in strs:
                temp.append([len(s), s])
            temp.sort()
            #print temp
            stack = temp[0][1]
            for s in temp[1:]:
                for i in range(len(stack)):
                    if s[1][i] == stack[i]:
                        continue
                    else:
                        stack = stack[0: i]
                        break
            result = stack
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.longestCommonPrefix(["longman", "longday", "longlong"])
    print s.longestCommonPrefix(["aa","a"])
    finish = clock()
    print (finish - start) * 1000