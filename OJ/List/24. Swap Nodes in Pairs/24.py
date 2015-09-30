# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
        	return None
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head
        while slow.next and fast.next:
        	slow.next = fast.next
        	temp = fast.next.next
        	fast.next.next = fast
        	fast.next = temp

        	fast = fast.next
        	slow = slow.next.next
        return dummy.next
        