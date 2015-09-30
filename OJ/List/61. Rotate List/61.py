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
        fast = head # tail
        slow = head# newHead
        length = 1 # number of nodes
        while fast.next: # get the number of nodes in the list
        	fast = fast.next
        	length += 1
        fast = head
        k = k % length
        while fast.next:
        	fast = fast.next
        	k -= 1
        	length += 1
        	if k < 0:
        		slow = slow.next
        temp = slow.next
        if not temp or k > 0:
        	return head
        else:
        	slow.next = None
        	fast.next = head
        	return temp

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
