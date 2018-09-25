# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p = ListNode(0)
        p.next = head
        head = p
        q = p.next
        i = 0
        p_head = head
        while i < m - 1:
            p_head = p_head.next
            i += 1
        q_head = p_head.next
        p_tail = p_head
        while i < n:
            p_tail = p_tail.next
            i += 1
        q_tail = p_tail.next
        qr = q_head.next
        while q_tail != p_tail:
            q_head.next = q_tail
            q_tail = q_head
            q_head = qr
            if qr:
                qr = qr.next
        p_head.next = q_tail
        return head.next


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(6)

    l4 = sol.reverseBetween(l1, 3, 6)
    print(l4.val)
    print(l4.next.val)
    print(l4.next.next.val)
    print(l4.next.next.next.val)
    print(l4.next.next.next.next.val)
    print(l4.next.next.next.next.next.val)