class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        def ksum(nums, k, target):
            i = 0
            if k == 2:
                j = len(nums) - 1
                while i < j:
                    if nums[i] + nums[j] == target:
                        yield (nums[i], nums[j])
                        i += 1
                    elif nums[i] + nums[j] > target:
                        j -= 1
                    else:
                        i += 1
            else:
                while i < len(nums) - k + 1:
                    newtarget = target - nums[i]
                    for sub in ksum(nums[i + 1: ], k - 1, newtarget):
                        yield (nums[i], ) + sub
                    i += 1
        return [list(t) for t in set(ksum(nums, 4, target))]
        
        


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.fourSum([1,0,-1,0,-2,2], 0)
    finish = clock()
    print (finish - start) * 1000