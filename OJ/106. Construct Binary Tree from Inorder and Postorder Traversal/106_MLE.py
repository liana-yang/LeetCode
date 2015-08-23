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
    def recursion(self, inorder, postorder, root):
        temp = None
        if postorder:
            length = len(postorder)
            temp = TreeNode(postorder[-1])
            i = inorder.index(temp.val)
            root = temp
            root.left = self.recursion(inorder[0: i], postorder[0: i], temp)
            root.right = self.recursion(inorder[i + 1:], postorder[i: length - 1], temp)

            '''print "temp: %s" % temp.val
            if root:
                print "root: %s" % root.val
            if root.left:
                print "left: %s" % root.left.val
            if root.right:
                print "right: %s" % root.right.val
            print "==="'''
        return temp

    def buildTree(self, inorder, postorder):
        root = None
        if postorder:
            #root = TreeNode(postorder[-1])
            root = self.recursion(inorder, postorder, root)
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