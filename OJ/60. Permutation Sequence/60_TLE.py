class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def recursion(self, nums, i, n, result):
        if i == n - 1:
            temp = []
            for k in range(0, n):
                temp.append(nums[k])
            result.append(temp)
        else:
            for k in range(i, n):
                temp = nums[k] #swap
                nums[k] = nums[i]
                nums[i] = temp

                self.recursion(nums, i + 1, n, result)

                temp = nums[k] #swap
                nums[k] = nums[i]
                nums[i] = temp

    def getPermutation(self, n, k):
        result = []
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        self.recursion(nums, 0, n, result)
        result.sort()
        s = ''
        for i in result[k - 1]:
            s += str(i)
        return s


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.getPermutation(9, 54494)
    finish = clock()
    print (finish - start) * 1000