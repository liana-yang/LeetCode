# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.

    # Splits in place a list in two halves, the first half is >= in size than the second.
    # @return A tuple containing the heads of the two halves
    def splitList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None
        return head, middle

    # Reverses in place a list.
    # @return the head of the new reversed list
    def reverseList(self, head):
        last = None
        cur = head # currentNode
        while cur:
            temp = cur.next # nextNode
            cur.next = last
            last = cur
            cur = temp
        return last

    # Merges in place two lists
    # @return The newly merged list.
    def mergeList(self, a, b):
        tail = a
        head = a
        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
        return head

    def reorderList(self, head):
        if not head or not head.next:
            return
        a, b = self.splitList(head)
        b = self.reverseList(b)
        head = self.mergeList(a, b)
        