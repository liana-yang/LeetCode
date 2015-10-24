# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        # based on level order traversal
        head = None # head of the next level
        pre = None # the leading node on the next level
        curr = root # current node of current level
        while curr:
            while curr: # iterate on the current level
            # left child
                if curr.left:
                    if pre:
                        pre.next = curr.left
                    else:
                        head = curr.left
                    pre = curr.left
            # right child
                if curr.right:
                    if pre:
                        pre.next = curr.right
                    else:
                        head = curr.right
                    pre = curr.right
            # move to the next node
                curr = curr.next
            # move to the next level
            curr = head
            head = None
            pre = None

