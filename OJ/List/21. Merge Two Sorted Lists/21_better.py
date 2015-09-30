# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
    	dummy = ListNode(0)
    	dummy.next = l1
    	cur = dummy
    	while l2:
    		while cur.next and cur.next.val <= l2.val: 
    			cur = cur.next # if the current list, l1, has a smaller value, then move cur forward
    		l1 = cur.next # otherwise, switch l1 and l2
    		cur.next = l2
    		l2 = l1
    	return dummy.next
