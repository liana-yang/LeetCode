# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(m - 1):
        	slow = slow.next
        newHead = slow
        slow = slow.next
        for i in range(n):
        	fast = fast.next
        newTail = fast.next
        if fast == slow:
        	return head
        	
        fast.next = None
        last = None
        cur = slow # currentNode
        while cur:
            temp = cur.next # nextNode
            cur.next = last
            last = cur
            cur = temp
        newHead.next = last
        slow.next = newTail
        return dummy.next


        