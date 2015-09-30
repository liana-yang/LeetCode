# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    def flatten(self, root):
        result = []
        stack = []
        p = root
        if p:
            stack.append(p)
        while stack:
            p = stack[0]
            result.append(p)
            del stack[0]
            if p.right and p.right.val != '#':
                stack.insert(0, p.right)
            if p.left and p.left.val != '#':
                stack.insert(0, p.left)
        if result:
            p = root
            for i in range(1, len(result)):
                p.left = None
                p.right = result[i]
                p = p.right
        
        '''for s in result:
            print s.val'''

if __name__=='__main__':
    from time import clock
    start = clock()
    root = TreeNode(1)
    v1 = TreeNode(2)
    v2 = TreeNode('#')
    v3 = TreeNode(3)
    v4 = TreeNode(4)
    v5 = TreeNode(5)
    #v6 = TreeNode(6)
    #v7 = TreeNode('#')
    #v8 = TreeNode('#')
    #v9 = TreeNode('#')
    #v10 = TreeNode(3)
    root.left = v1
    root.right = v2
    v1.left = v3
    v1.right = v4
    v3.left = v5
    #v2.right = v6
    #v3.left = v7
    #v3.right = v8
    #v4.left = v9
    #v4.right = v10
    s = Solution()
    s.flatten(root)
    finish = clock()
    print (finish - start) * 1000