# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slower = head
        faster = head
        while True:
            if faster == None or faster.next == None:
                return None
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                break
        slower = head
        while True:
        	if slower == faster:
        		return slower
        	else:
        		slower = slower.next
                faster = faster.next
        """
        using two pointers, one of them one step at a time. another pointer each take two steps. 
        Suppose the first meet at step k,the length of the Cycle is r. so..2k-k=nr,k=nr 
        Now, the distance between the start node of list and the start node of cycle is s. 
        the distance between the start of list and the first meeting node is k
        (the pointer which wake one step at a time waked k steps).
        the distance between the start node of cycle and the first meeting node is m, 
        so...s=k-m, s=nr-m=(n-1)r+(r-m),here we takes n = 1..so, 
        using one pointer start from the start node of list, 
        another pointer start from the first meeting node, 
        all of them wake one step at a time, 
        the first time they meeting each other is the start of the cycle.
        """