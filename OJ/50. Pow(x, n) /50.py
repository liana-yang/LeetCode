class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            n = - n
            x = 1 / x
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.myPow(2,3)
    print s.myPow(0.00001, 2147483647)
    finish = clock()
    print (finish - start) * 1000