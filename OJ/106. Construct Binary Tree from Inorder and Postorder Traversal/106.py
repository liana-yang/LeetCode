# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
   
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        i = inorder.index(root.val)

        root.right = self.buildTree(inorder[i + 1:], postorder)
        root.left = self.buildTree(inorder[0: i], postorder)

        return root


if __name__=='__main__':
    from time import clock
    start = clock()
    v1 = TreeNode(1)
    v2 = TreeNode(2)
    v3 = TreeNode(3)
    v4 = TreeNode(4)
    v5 = TreeNode(5)
    v6 = TreeNode(6)
    v7 = TreeNode(7)
    s = Solution()
    #s.buildTree([v1,v2,v3,v4,v5,v6,v7,v8],[v1,v3,v4,v2,v6,v8,v7,v5])
    print s.buildTree([4,5,2,7,6,1,3],[5,4,7,6,2,3,1]).val
    finish = clock()
    print (finish - start) * 1000