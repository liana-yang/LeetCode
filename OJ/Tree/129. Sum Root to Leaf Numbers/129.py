# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        if not root:
        	return 0
        stackOfNode = [root]
        stackOfString = [root.val]
        while stackOfNode:
        	currNode = stackOfNode.pop()
        	currString = stackOfString.pop()
        	if currNode.left:
        		stackOfNode.append(currNode.left)
        		stackOfString.append(currString * 10 + currNode.left.val)
        	if currNode.right:
        		stackOfNode.append(currNode.right)
        		stackOfString.append(currString * 10 + currNode.right.val)
        	if not currNode.left and not currNode.right:
        		result.append(currString)
        return sum(result)