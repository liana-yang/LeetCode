class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        import re
        str = str.strip() #remove whitespaces
        str = re.findall('(^[\+\-0]*\d+)', str)
        print str
        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = - 2147483648
            if result > MAX_INT:
                return MAX_INT
            elif result < MIN_INT:
                return MIN_INT
            else:
                return result
        except:
            return 0


if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()        
    print s.myAtoi('      -11919730356x')
    print s.myAtoi('1')
    finish = clock()
    print (finish - start) * 1000
