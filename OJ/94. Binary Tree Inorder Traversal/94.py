# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def recursion(self, root, result):
        if root and root.val != '#':
            self.recursion(root.left, result)
            result.append(root.val)
            self.recursion(root.right, result)

    def inorderTraversal(self, root):
        result = []
        if root:
            self.recursion(root, result)
        #print result
        return result


if __name__=='__main__':
    from time import clock
    start = clock()
    root = TreeNode(1)
    v1 = TreeNode('#')
    v2 = TreeNode(2)
    v3 = TreeNode(3)
    root.left = v1
    root.right = v2
    v2.left = v3
    s = Solution()
    print s.inorderTraversal(root)
    finish = clock()
    print (finish - start) * 1000