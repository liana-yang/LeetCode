# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}

    def inorderTraversal(self, root):
        result = []
        stack = []
        p = root
        while (p != None and p.val != '#') or stack:
            while p != None and p.val != '#':
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                result.append(p.val)
                p = p.right
        return result



if __name__=='__main__':
    from time import clock
    start = clock()
    root = TreeNode(1)
    v1 = TreeNode('#')
    v2 = TreeNode(2)
    v3 = TreeNode(3)
    root.left = v1
    root.right = v2
    v2.left = v3
    s = Solution()
    print s.inorderTraversal(root)
    finish = clock()
    print (finish - start) * 1000