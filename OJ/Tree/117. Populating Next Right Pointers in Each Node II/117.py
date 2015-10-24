# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def recursion(self, root, depth, result):
        if not root:
            return
        if len(result) == depth:
            result.append([])
        result[depth].append(root)
        self.recursion(root.left, depth + 1, result)
        self.recursion(root.right, depth + 1, result)

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        result = []
        self.recursion(root, 0, result)
        for i in range(len(result)):
        	for j in range(len(result[i]) - 1):
        		result[i][j].next = result[i][j + 1]
        # return result