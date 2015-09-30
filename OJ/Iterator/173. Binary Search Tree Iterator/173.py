# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# I use Stack to store directed left children from root. 
# When next() be called, I just pop one element and process its right child as new root. 
# The code is pretty straightforward.
# So this can satisfy O(h) memory, hasNext() in O(1) time, and next() is O(1) time.


So this can satisfy O(h) memory, hasNext() in O(1) time, But next() is O(h) time.
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left
        

# Your BSTIterator will be called like this:
root = TreeNode(0)
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())