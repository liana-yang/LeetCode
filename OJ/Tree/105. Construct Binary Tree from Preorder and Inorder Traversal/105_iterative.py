# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer[]} inorder
    # @param {integer[]} postorder
    # @return {TreeNode}
   
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None
        p = None
        root = TreeNode(preorder[0])
        del preorder[0]
        stack = [root]

        while True:
            if inorder[0] == stack[-1].val:
                p = stack.pop()
                del inorder[0]
                if not inorder:
                    break
                if stack and inorder[0] == stack[-1].val:
                    continue
                p.right = TreeNode(preorder[0])
                del preorder[0]
                stack.append(p.right)
            else:
                p = TreeNode(preorder[0])
                del preorder[0]
                stack[-1].left = p
                stack.append(p)
        return root
        # https://leetcode.com/discuss/2297/the-iterative-solution-is-easier-than-you-think