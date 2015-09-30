# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
    	if not head or k == 1:
    		return head
    	num = 0
    	dummy = ListNode(0)
    	dummy.next = head
    	cur = dummy
    	nex = dummy
    	pre = dummy
    	while cur.next:
    		num += 1
    		cur = cur.next
    	while num >= k:
    		cur = pre.next
    		nex = cur.next
    		for i in range(1, k):
    			cur.next = nex.next
    			nex.next = pre.next
    			pre.next = nex
    			nex = cur.next
    		pre = cur
    		num -= k
    	return dummy.next
        