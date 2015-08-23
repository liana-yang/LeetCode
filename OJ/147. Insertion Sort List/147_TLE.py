# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if not head:
            return None
        node = head.next
        head.next = None
        p = head
        if node:
            while node:
                while p:
                    #print "node = %s, p = %s" % (node.val, p.val)
                    if node.val >= p.val:
                        if p.next:
                            if node.val >= p.next.val:
                                p = p.next
                            else:
                                temp = node.next
                                node.next = p.next
                                p.next = node
                                p = head
                                node = temp
                                break
                        else:
                            temp = node.next
                            node.next = None
                            p.next = node
                            p = head
                            node = temp
                            break
                    else:
                        temp = node.next
                        node.next = head
                        head = node
                        p = head
                        node = temp
                        break
        return head

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    l1 = ListNode(3)
    l2 = ListNode(4)
    l3 = ListNode(1)
    l4 = ListNode(3)

    l1.next = l2
    l2.next = l3
    #l3.next = l4
    print s.insertionSortList(l1).next.next.val
    finish = clock()
    print (finish - start) * 1000