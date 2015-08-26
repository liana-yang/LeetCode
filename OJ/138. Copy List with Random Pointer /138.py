# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        next = None
        # first round: make copy of each node,
        # and link them together side-by-side in a single list.
        while p:
            next = p.next
            copy = RandomListNode(p.label)
            p.next = copy
            copy.next = next
            p = next
        # second round: assign random pointers for the copy nodes.
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        # third round: restore the original list, and extract the copy list.
        p = head
        pseudoHead = RandomListNode(0)
        copy = None
        copyP = pseudoHead
        while p:
            next = p.next.next
            # extract the copy
            copy = p.next
            copyP.next = copy
            copyP = copy
            # restore the original list
            p.next = next
            p = next

        return pseudoHead.next


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    head = RandomListNode(1)
    l1 = RandomListNode(2)
    l2 = RandomListNode(3)
    head.next = l1
    l1.next = l2
    head.random = l2
    l1.random = l2
    l2.random = l1
    print s.copyRandomList(head)
    finish = clock()
    print (finish - start) * 1000