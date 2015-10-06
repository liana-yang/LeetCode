# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre1 = dummy
        curr1 = head
        while curr1:
            pre2 = curr1
            curr2 = curr1.next
            while curr2:
            	if curr2.val >= curr1.val:
            		curr2 = curr2.next
            		pre2 = pre2.next
            	else:
            		temp = curr2.next
            		pre1.next = curr2
            		curr2.next = curr1
            		pre2.next = temp
            		pre1 = curr2
            		curr2 = temp
            curr1 = curr1.next
            pre1 = pre1.next
        return dummy.next