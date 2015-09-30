# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def helper(self, left, right):
		if not left or not right:
			return left == right
		if left.val != right.val:
			return False
		return self.helper(left.left, right.right) and self.helper(left.right, right.left)

	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		return not root or self.helper(root.left, root.right)


        