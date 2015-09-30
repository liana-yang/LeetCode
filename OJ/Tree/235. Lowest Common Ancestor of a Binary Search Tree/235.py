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
        if not root:
        	return None
        if p.val > q.val: # make sure p < q
        	p, q = q, p
        if p.val == root.val or q.val == root.val:
        	return root
        elif p.val < root.val:
        	if q.val > root.val:
        		return root
        	else:
        		return self.lowestCommonAncestor(root.left, p, q)
        else:
        	return self.lowestCommonAncestor(root.right, p, q)
