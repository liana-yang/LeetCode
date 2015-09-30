# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        result = []
        count = 0

        stack = []
        p = root
        LastVisited = None

        if root:
            while (p != None and p.val != '#') or stack:
                while p != None:
                    stack.append(p)
                    count += 1
                    p = p.left
                p = stack[-1]
                if p.left == None and p.right == None:
                    result.append(count)
                if p.right == None or LastVisited == p.right:
                    LastVisited = p
                    stack.pop()
                    count -= 1
                    p = None
                else:
                    p = p.right
            return min(result)
        else:
            return 0

s = Solution()
print s.minDepth(TreeNode(1))