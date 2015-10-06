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
        pre = dummy
        curr = head
        count = dummy
        while count.next:
        	while curr.next:
        		if curr.val > curr.next.val:
        			temp = curr.next.next
        			pre.next = curr.next
        			curr.next.next = curr
        			curr.next = temp
        			pre = pre.next
        		else:
        			pre = pre.next
        			curr = curr.next
        	pre = count
        	curr = count.next
        	count = count.next
        return dummy.next