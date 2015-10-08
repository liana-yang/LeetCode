# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateSubtrees(self, s, e):
        res = []
        if s > e:
            res.append(None) # empty tree
            return res
        for i in range(s, e + 1):
            leftSubtrees = self.generateSubtrees(s, i - 1)
            rightSubtrees = self.generateSubtrees(i + 1, e)
            for left in leftSubtrees:
                for right in rightSubtrees:
                    root = TreeNode(i)
                    root.left = left
                    root. right = right
                    res.append(root)
        return res

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateSubtrees(1, n)

        # divide-and-conquer
        