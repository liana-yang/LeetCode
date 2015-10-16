# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def recursion(self, root, maxPath, result):
        if not root:
            return 0
        left = max(0, self.recursion(root.left, maxPath, result))
        right = max(0, self.recursion(root.right, maxPath, result))
        #maxPath = max(maxPath, left + right + root.val)
        result.append(left + right + root.val)
        return root.val + max(left, right)

    def maxPathSum(self, root):
        result = []
        maxPath = -2147483648
        self.recursion(root, maxPath, result)
        return max(result)
        

        


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l1.left = l2
    l2.left = l3
    print s.maxPathSum(l1)
    finish = clock()
    print (finish - start) * 1000