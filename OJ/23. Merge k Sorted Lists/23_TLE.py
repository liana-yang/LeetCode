# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        head1 = l1
        head2 = l2
        while head1 and head2:
            if head2.val >= head1.val:
                if head1.next:
                    if head2.val <= head1.next.val:
                        temp1 = head1.next
                        temp2 = head2.next
                        head1.next = head2
                        head2.next = temp1
                        head1 = head1.next
                        head2 = temp2
                    else:
                        head1 = head1.next
                else:
                    head1.next = head2
                    t = l1
                    return l1
            else:
                temp2 = head2.next
                head2.next = head1
                l1 = head2
                head1 = l1
                head2 = temp2
        if l1 == None:
            l1 = l2
            
        return l1

    def mergeKLists(self, lists):
        if lists:
            result = lists[0]
            for i in range(1, len(lists)):
                result = self.mergeTwoLists(result, lists[i])
                '''t = result
                while t:
                    print t.val
                    t = t.next
                print "======"'''
        else:
            result = lists
        return result


if __name__=='__main__':
    from time import clock
    start = clock()
    l1 = ListNode(2)
    v1 = ListNode(5)
    v2 = ListNode(7)

    l2 = ListNode(8)
    v4 = ListNode(9)
    v5 = ListNode(10)

    l3 = ListNode(3)
    v6 = ListNode(4)
    v7 = ListNode(5)

    l1.next = v1
    v1.next = v2

    l2.next = v4
    v4.next = v5

    l3.next = v6
    v6.next = v7

    lists = [l1, l2, l3]

    s = Solution()
    s.mergeKLists(lists)
    finish = clock()
    print (finish - start) * 1000