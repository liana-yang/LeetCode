class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    #def recursion(self, nums, i, n, result):
        

    def getPermutation(self, n, k):
        import math
        result = ''
        digit = [1,2,3,4,5,6,7,8,9]
        digit = digit[0: n]
        i = n - 1
        while k > 0:
            num = k / math.factorial(i)
            k -= num * math.factorial(i)
            if k == 0:
                num -= 1
            result += str(digit[num])
            del digit[num]
            
            i -= 1
        while digit:
            result += str(digit.pop())
        return result



if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.getPermutation(9,54494)
    print s.getPermutation(3,5)
    finish = clock()
    print (finish - start) * 1000