# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
        	return result
        queue = [root]
        while queue:
        	levelNum = len(queue)
        	temp = []
        	for i in range(levelNum):
        		cur = queue[0]
        		temp.append(cur.val)
        		if cur.left:
        			queue.append(cur.left)
        		if cur.right:
        			queue.append(cur.right)
        		del queue[0]
        	result.append(temp)
        return list(reversed(result))

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
print s.levelOrderBottom(l1)