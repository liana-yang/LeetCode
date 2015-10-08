# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # https://leetcode.com/discuss/13034/no-fancy-algorithm-just-simple-and-powerful-order-traversal
        self.firstElement = None
        self.secondElement = None
        # The reason for this initialization is to avoid null pointer exception in the first comparison 
        # when prevElement has not been initialized
        self.prevElement = TreeNode(-2147483648)

        def traverse(root):
            if root:
                traverse(root.left)
                # Start of "do some business", 
                # If first element has not been found, assign it to prevElement (refer to 6 in the example above)
                if not self.firstElement and self.prevElement.val >= root.val:
                    self.firstElement = self.prevElement
                # If first element is found, assign the second element to the root (refer to 2 in the example above)
                if self.firstElement and self.prevElement.val >= root.val:
                    self.secondElement = root
                self.prevElement = root
                traverse(root.right)

        # In order traversal to find the two elements
        traverse(root)
        # Swap the values of the two nodes
        if self.firstElement and self. secondElement:
            self.firstElement.val, self.secondElement.val = self.secondElement.val, self.firstElement.val
