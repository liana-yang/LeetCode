# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if head:
            length = - 1
            end = head
            while(end):
                end = end.next
                length += 1
        
            i = 0
            start = head
            end = head
            while(i < length / 2):
                end = end.next
                i += 1

            new = end
            end = end.next
            new.next = None
            while(end):
                temp = end.next
                end.next = new
                new = end
                end = temp
            i += 1
            while(i <= length):
                temp1 = start.next
                temp2 = new.next
                start.next = new
                start = temp1
                new.next = start
                new = temp2
                i += 1

if __name__=='__main__':
    from time import clock
    start = clock()
    l1 = ListNode(1)
    v1 = ListNode(2)
    v2 = ListNode(3)
    v3 = ListNode(4)
    v4 = ListNode(5)
    v5 = ListNode(6)
    l1.next = v1
    v1.next = v2
    v2.next = v3
    v3.next = v4
    v4.next = v5


    s = Solution()
    s.reorderList(l1)
    finish = clock()
    print (finish - start) * 1000