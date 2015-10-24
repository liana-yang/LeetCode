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
        if root:
            pre = root
            cur = None
            while pre.left:
                cur = pre
                while cur:
                    cur.left.next = cur.right
                    if cur.next:
                        cur.right.next = cur.next.left
                    cur = cur.next
                pre = pre.left
