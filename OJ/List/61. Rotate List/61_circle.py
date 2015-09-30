# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
        	return head
        newHead = head
        tail = head
        length = 1 # number of nodes
        while tail.next: # get the number of nodes in the list
        	tail = tail.next
        	length += 1
        tail.next = head
        k = k % length
        if k:
            for i in range(length - k):
                tail = tail.next
        newHead = tail.next
        tail.next = None
        return newHead

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
print s.rotateRight(l1, 2).val
