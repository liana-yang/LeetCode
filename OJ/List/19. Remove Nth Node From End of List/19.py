# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # A one pass solution can be done using pointers. 
        # Move one pointer fast --> n+1 places forward, 
        # to maintain a gap of n between the two pointers and then move both at the same speed. 
        # Finally, when the fast pointer reaches the end, 
        # the slow pointer will be n+1 places behind 
        # - just the right spot for it to be able to skip the next node.
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        # Move fast in front so that the gap between slow and fast becomes n
        for i in range(n + 1):
        	fast = fast.next
        # Move fast to the end, maintaining the gap
        while fast:
        	slow = slow.next
        	fast = fast.next
        # Skip the desired node
        slow.next = slow.next.next
        return dummy.next
