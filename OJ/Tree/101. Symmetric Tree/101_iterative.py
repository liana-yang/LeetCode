# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		# use stack
		if not root:
			return True
		stack = []
		left = None
		right = None
		if root.left:
			if not root.right:
				return False
			stack.append(root.left)
			stack.append(root.right)
		elif root.right:
			return False

		while stack:
			if len(stack) % 2 != 0:
				return False
			right = stack.pop()
			left = stack.pop()
			if right.val != left.val:
				return False
			if left.left:
				if not right.right:
					return False
				stack.append(left.left)
				stack.append(right.right)
			elif right.right:
				return False

			if left.right:
				if not right.left:
					return False
				stack.append(left.right)
				stack.append(right.left)
			elif right.left:
				return False
		return True
        