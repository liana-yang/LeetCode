class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        maxNum = 2147483647
        minNum = - maxNum - 1
        result = 0
        sig = 1
        if x < 0:
            sig = - 1
        x = abs(x)
        while x > 0:
            result = result * 10 + x % 10
            x /= 10
        result *= sig

        if result < minNum or result > maxNum:
            return 0
        return result


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.reverse(1534236469)
    finish = clock()
    print (finish - start) * 1000