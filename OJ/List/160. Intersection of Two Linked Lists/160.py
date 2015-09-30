# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        if not p1 or not p2:
        	return None
        while p1 and p2 and p1 != p2:
        	p1 = p1.next
        	p2 = p2.next
        	# Any time they collide or reach end together without colliding 
    		# then return any one of the pointers.
        	if p1 == p2:
        		return p1
        	# If one of them reaches the end earlier then reuse it 
        	# by moving it to the beginning of other list.
        	# Once both of them go through reassigning, 
        	# they will be equidistant from the collision point.
        	if not p1:
        		p1 = headB
        	if not p2:
        		p2 = headA
        return p1
        