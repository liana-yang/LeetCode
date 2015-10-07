# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = head
        while curr:
        	if curr.val == val:
        		temp = curr.next
        		pre.next = temp
        		curr.next = None
        		curr = temp
        	else:
        		pre = pre.next
        		curr = curr.next
        return dummy.next
        