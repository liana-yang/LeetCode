class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0 for n in nums]
        temp = 1
        length = len(nums)
        for i in range(length):
            result[i] = temp
            temp *= nums[i]
        temp = 1
        for i in range(length):
            result[length - i - 1] *= temp
            temp *= nums[length - i - 1]
        return result
    # Use tmp to store temporary multiply result by two directions. 
    # Then fill it into result. 

s = Solution()
print s.productExceptSelf([1,0])