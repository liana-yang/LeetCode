class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}

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
    def permute(self, nums):
        result = []
        self.recursion(nums, 0, len(nums), result)
        return result


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.permute([1,2,3])
    finish = clock()
    print (finish - start) * 1000