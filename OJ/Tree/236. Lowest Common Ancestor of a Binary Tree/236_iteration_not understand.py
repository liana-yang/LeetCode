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
        # It's recursive and expands the meaning of the function. 
        # If the current (sub)tree contains both p and q, 
        # then the function result is their LCA. 
        # If only one of them is in that subtree, 
        # then the result is that one of them. 
        # If neither are in that subtree, the result is null/None/nil.

        # Same algorithm as my recursive solution, but iterative. 
        # I do a post-order traversal with a stack. 
        # Each stack element at first is a [node, parent] pair, 
        # where parent is the stack element of the node's parent node. 
        # When the children of a parent get finished, 
        # their results are appended to their parent's stack element. 
        # So when a parent gets finished, 
        # we have the results of its children/subtrees available 
        # (its stack element at that point is [node, parent, resultForLeftSubtree, resultForRightSubtree]).
        answer = []
        stack = [[root, answer]]
        while stack:
            top = stack.pop()
            (node, parent), subs = top[:2], top[2:]
            if node in (None, p, q):
                parent += node
            elif not subs:
                stack += top, [node.right, top], [node.left, top]
            else:
                if all(subs):
                    parent += [node]
                else:
                    parent += [max(subs)]
        return answer[0]

       
