class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        stack = []
        dict = {']': '[', '}': '{', ')': '('}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()        
    #s.isValid('[({(())}[()])]')
    print s.isValid('[()](())')
    #s.isValid('([]]')
    #s.isValid('()[]{}')
    #s.isValid('([])')
    finish = clock()
    print (finish - start) * 1000