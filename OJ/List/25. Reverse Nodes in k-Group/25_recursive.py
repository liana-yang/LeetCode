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
    	cur = head
        count = 0
        while cur and count != k: # find the k+1 node
            cur = cur.next
            count += 1
        if count == k: # if k+1 node is found
            cur = self.reverseKGroup(cur, k) # reverse list with k+1 node as head
            # head - head-pointer to direct part, 
            # curr - head-pointer to reversed part
            while count > 0: # reverse current k-group: 
                count -= 1
                temp = head.next # tmp - next head in direct part
                head.next = cur # preappending "direct" head to the reversed list 
                cur = head # move head of reversed part to a new node
                head = temp # move "direct" head to the next node in direct part
            head = cur
        return head

        