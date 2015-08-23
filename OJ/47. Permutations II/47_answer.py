class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def duplicated(self, nums, i, j):
        for t in range(i, j):
            if nums[t] == nums[j]:
                return False
        return True

    def recursion(self, nums, i, n, result):
        if i == n - 1:
            temp = []
            for k in range(0, n):
                temp.append(nums[k])
            result.append(temp)
        else:
            for k in range(i, n):
                if self.duplicated(nums, i ,k):
                    temp = nums[k] #swap
                    nums[k] = nums[i]
                    nums[i] = temp

                    self.recursion(nums, i + 1, n, result)

                    temp = nums[k] #swap
                    nums[k] = nums[i]
                    nums[i] = temp

    def permuteUnique(self, nums):
        result = []
        self.recursion(nums, 0, len(nums), result)
        return result


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.permuteUnique([1,1,3])
    finish = clock()
    print (finish - start) * 1000