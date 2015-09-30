class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        n = len(str(x))
        i = 0
        while i < n:
            temp = x % 10
            if str(x)[i] != str(temp):
                return False
            x = (x - temp) / 10
            i += 1
            n -= 1
        return True




if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.isPalindrome(1234321)
    finish = clock()
    print (finish - start) * 1000