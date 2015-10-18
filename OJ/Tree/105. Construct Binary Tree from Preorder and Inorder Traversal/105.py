# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        root.right = self.buildTree(preorder[i + 1:], inorder[i + 1:])
        root.left = self.buildTree(preorder[1: i + 1], inorder[0: i])

        return root
        
s = Solution()
print s.buildTree([1,4,2,3],[1,2,3,4])