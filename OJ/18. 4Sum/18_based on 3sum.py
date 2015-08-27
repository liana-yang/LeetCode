class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(0, len(nums) - 2):
            if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                newTarget = target - nums[i]
                for j in range(i + 1, len(nums) - 1):
                    if j == i + 1 or (j > i + 1 and nums[j] != nums[j - 1]):
                        lo = j + 1
                        hi = len(nums) - 1
                        sum = newTarget - nums[j]
                        while lo < hi:
                            if nums[lo] + nums[hi] == sum:
                                result.append([nums[i], nums[j], nums[lo], nums[hi]])
                                while lo < hi and nums[lo] == nums[lo + 1]:
                                    lo += 1
                                while lo < hi and nums[hi] == nums[hi - 1]:
                                    hi -= 1
                                lo += 1
                                hi -= 1
                            elif nums[lo] + nums[hi] < sum:
                                lo += 1
                            else:
                                hi -= 1
        return result

        
        


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.fourSum([-1,0,1,2,-1,-4], -1)
    finish = clock()
    print (finish - start) * 1000