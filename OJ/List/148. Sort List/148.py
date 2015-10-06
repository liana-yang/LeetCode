# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
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

    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0:
        	return None
        if length == 1:
        	return lists[0]
        if length == 2:
        	return self.mergeTwoLists(lists[0], lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[0: length / 2]), self.mergeKLists(lists[length / 2: length]))

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
        	return head
        lists = [head]
        curr = head
        while curr:
        	if curr.next and curr.val > curr.next.val:
        		temp = curr.next
        		curr.next = None
        		lists.append(temp)
        		curr = temp
        	else:
        		curr = curr.next
        return self.mergeKLists(lists)

