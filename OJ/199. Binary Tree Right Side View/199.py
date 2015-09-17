# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
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
        	result.append(temp[-1])
        return result
        