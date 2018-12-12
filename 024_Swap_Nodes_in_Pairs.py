# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        p.next = head
        head = p
        q = p.next
        while p.next and q.next:
            p.next = q.next
            q.next = p.next.next
            p.next.next = q

            p = p.next.next
            q = p.next
        return head.next


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)

    l4 = sol.swapPairs(l1)
    print(l4.val)
    print(l4.next.val)
    print(l4.next.next.val)
    print(l4.next.next.next.val)
    print(l4.next.next.next.next.val)
