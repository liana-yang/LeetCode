# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # the idea is to use stack for preorder traverse
        stack = [(p,q)]
        while stack :
            x,y = stack.pop()
            if x == None and y ==None:
                continue
            if x == None or y == None:
                return False
            if x.val == y.val:
                stack.append((x.left,y.left))
                stack.append((x.right,y.right))
            else:
                return False
        return True
        