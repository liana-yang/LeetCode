# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        cur = head # currentNode
        while cur:
            temp = cur.next # nextNode
            cur.next = last
            last = cur
            cur = temp
        return last

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        faster = head
        slower = head
        while faster.next and faster.next.next:
        	faster = faster.next.next
        	slower = slower.next
        temp = slower.next
        head2 = self.reverseList(temp)
        head1 = head
        while head2:
            if head2.val != head1.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True


        