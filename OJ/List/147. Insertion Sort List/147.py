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
        last = head
        p = head
        node = head.next
        while node:
            if node.val >= last.val:
                last = node
                node = node.next
            elif node.val <= head.val:
                temp = node.next
                node.next = head
                head = node
                p = head
                last.next = temp
                node = temp
            else:
                while p is not last:
                    if node.val >= p.next.val:
                        p = p.next
                    else:
                        temp1 = node.next
                        temp2 = p.next
                        p.next = node
                        node.next = temp2
                        last.next = temp1
                        node = temp1
                        p = head
                        break
        return head

if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    l1 = ListNode(4)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(3)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    print s.insertionSortList(l1).next.next.next.val
    finish = clock()
    print (finish - start) * 1000