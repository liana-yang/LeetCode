class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        sign = 1
        start = False
        length = 0
        result = 0

        for i in range(len(str)):
            if str[i] == '+':
                if start == False:
                    sign = 1
                    start = True
                else:
                    sign = 0
                    break
            elif str[i] == '-':
                if start == False:
                    sign = - 1
                    start = True
                else:
                    sign = 0
                    break
            elif '0' <= str[i] <= '9':
                if start == False:
                    start = True

                if result > 214748363:
                    if result == 214748364:
                        if int(str[i]) > 7 and sign == 1:
                            result = result * 10 + 7
                        elif int(str[i]) > 8 and sign == - 1:
                            result = result * 10 + 8
                        else:
                            result = result * 10 + int(str[i])
                    elif sign == 1:
                        result = 2147483647
                    elif sign == - 1:
                        result = 2147483648
                else:
                    result = result * 10 + int(str[i])
                length += 1
            else:
                if start == True:
                    break
                elif str[i] != ' ':
                    sign = 0
                    break
        result *= sign

        print "sign = %s" % sign
        print result
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()        
    s.myAtoi('      -11919730356x')
    finish = clock()
    print (finish - start) * 1000
