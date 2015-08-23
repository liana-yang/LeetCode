# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def recursion(self,root):
        result = []
        stack = []
        p = root
        LastVisited = None
        s = 0
        if root:
            while (p != None and p.val != '#') or stack:
                while p != None:
                    stack.append(p)
                    s += p.val
                    p = p.left
                p = stack[-1]
                if p.left == None and p.right == None:
                    result.append(s)
                if p.right == None or LastVisited == p.right:
                    LastVisited = p
                    stack.pop()
                    s -= p.val
                    p = None
                else:
                    p = p.right
            temp = max(result)
            result.remove(temp)
            if result:
                return max(result) + temp - root.val
            else:
                return temp
        else:
            return 0
    def maxPathSum(self, root):
        nodes = []
        stack = []
        p = root
        while (p != None and p.val != '#') or stack:
            while p != None and p.val != '#':
                nodes.append(p)
                stack.append(p)
                p = p.left
            if stack:
                p = stack.pop()
                p = p.right
        result = []
        for node in nodes:
            result.append(self.recursion(node))
        return max(result)

        


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l1.left = l2
    l2.left = l3
    print s.maxPathSum(l1)
    finish = clock()
    print (finish - start) * 1000