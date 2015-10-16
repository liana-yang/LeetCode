# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isValidBST(self, root):
        result = True
        stack = []
        p = root
        pre = None
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                temp = stack.pop()
                if pre and temp.val <= pre.val:
                    return False
                pre = temp
                p = temp.right
        return result



if __name__=='__main__':
    from time import clock
    start = clock()
    root = TreeNode(3)
    v1 = TreeNode(1)
    v2 = TreeNode(5)
    v3 = TreeNode(0)
    v4 = TreeNode(2)
    v5 = TreeNode(4)
    v6 = TreeNode(6)
    v7 = TreeNode('#')
    v8 = TreeNode('#')
    v9 = TreeNode('#')
    v10 = TreeNode(3)
    root.left = v1
    root.right = v2
    v1.left = v3
    v1.right = v4
    v2.left = v5
    v2.right = v6
    v3.left = v7
    v3.right = v8
    v4.left = v9
    v4.right = v10
    s = Solution()
    print s.isValidBST(root)
    finish = clock()
    print (finish - start) * 1000