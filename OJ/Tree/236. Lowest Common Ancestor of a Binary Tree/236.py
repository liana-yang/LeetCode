# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # It's recursive and expands the meaning of the function. 
        # If the current (sub)tree contains both p and q, 
        # then the function result is their LCA. 
        # If only one of them is in that subtree, 
        # then the result is that one of them. 
        # If neither are in that subtree, the result is null/None/nil.
        
        if root in (None, p, q):
        	return root
        left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
        if left and right:
        	return root
        else:
        	return left or right
