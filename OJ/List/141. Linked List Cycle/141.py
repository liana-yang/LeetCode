
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        slower = head
        faster = head
        while True:
            if faster == None or faster.next == None:
                return False
            slower = slower.next
            faster = faster.next.next
            if slower == faster:
                return True

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
    print s.hasCycle(l1)
    finish = clock()
    print (finish - start) * 1000