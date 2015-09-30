# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
	def recursion(self, root, depth, result):
		if not root:
			return
		if len(result) == depth:
			result.append([])
		result[depth].append(root.val)
		self.recursion(root.left, depth + 1, result)
		self.recursion(root.right, depth + 1, result)

	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		result = []
		self.recursion(root, 0, result)
		return result

s = Solution()
l1 = TreeNode(3)
l2 = TreeNode(9)
l3 = TreeNode(20)
l4 = TreeNode(15)
l5 = TreeNode(7)

l1.left = l2
l1.right = l3
l3.left = l4
l3.right = l5
print s.levelOrder(l1)
