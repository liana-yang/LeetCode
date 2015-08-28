class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        sign = 1
        result = 0
        i = 0
        if not str:
            return 0
        while str[i] == ' ':
            i += 1
        if str[i] == '-' or str[i] == '+':
            sign = 1 - 2 * (str[i] == '-')
            i += 1
        while i < len(str) and '0' <= str[i] <= '9':
            if result > 2147483647 / 10 or (result == 2147483647 / 10 and str[i] > '7'):
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648
            result = 10 * result + int(str[i])
            i += 1
        return result * sign

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
