# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, total):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        stackOfNode = [root]
        stackOfString = [[root.val]]
        while stackOfNode:
            currNode = stackOfNode.pop()
            currString = stackOfString.pop()
            if currNode.left:
                stackOfNode.append(currNode.left)
                stackOfString.append(currString + [currNode.left.val])
            if currNode.right:
                stackOfNode.append(currNode.right)
                stackOfString.append(currString + [currNode.right.val])
            if not currNode.left and not currNode.right and sum(currString) == total:
                result.append(currString)
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    root = TreeNode(1)
    v1 = TreeNode(2)
    v2 = TreeNode(3)
    v3 = TreeNode(4)
    v4 = TreeNode(5)
    v5 = TreeNode(6)
    v6 = TreeNode(7)
    v7 = TreeNode(8)
    v8 = TreeNode(9)
    v9 = TreeNode(10)
    v10 = TreeNode(11)
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
    print s.pathSum(root, 22)
    finish = clock()
    print (finish - start) * 1000
        