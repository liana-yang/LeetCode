class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}     
        i = 1
        while i <= len(nums):
            table.update({nums[i - 1]: i})
            i += 1
        for i in range(1, len(nums) + 1):
            if table.has_key(target - nums[i - 1]) and table[target - nums[i - 1]] != i:
                return sorted([table[target - nums[i - 1]], i])
        
        


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.twoSum([2,7,1,3], 9)
    finish = clock()
    print (finish - start) * 1000