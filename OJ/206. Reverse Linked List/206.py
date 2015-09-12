# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        cur = head # currentNode
        while cur:
            temp = cur.next # nextNode
            cur.next = last
            last = cur
            cur = temp
        return last

        