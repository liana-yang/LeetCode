# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
            
        return root


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.sortedArrayToBST([1,2,3,4]).right.val
    finish = clock()
    print (finish - start) * 1000