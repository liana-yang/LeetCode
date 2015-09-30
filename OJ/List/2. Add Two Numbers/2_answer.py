# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        temp = 0
        result = ListNode(0)
        s = result
        while l1 or l2 or temp:
            s.val = temp
            if l1:
                s.val += l1.val
                l1 = l1.next
            if l2:
                s.val += l2.val
                l2 = l2.next
            temp, s.val = divmod(s.val, 10)
            if l1 or l2 or temp:
                s.next = ListNode(0)
                s = s.next
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    l1 = ListNode(2)
    v1 = ListNode(4)
    v2 = ListNode(3)
    l1.next = v1
    v1.next = v2

    l2 = ListNode(5)
    v1 = ListNode(6)
    v2 = ListNode(4)
    l2.next = v1
    v1.next = v2

    s = Solution()
    s.addTwoNumbers(l1, l2)
    finish = clock()
    print (finish - start) * 1000