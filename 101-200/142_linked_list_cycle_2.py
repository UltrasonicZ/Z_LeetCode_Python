# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        q = head
        while q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                return p
        return None


if __name__ == "__main__":
    sol = Solution()
    l1 = []
    # l1 = ListNode(1)
    # l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)
    # l1.next.next.next.next = ListNode(5)
    # l1.next.next.next.next.next = ListNode(6)
    # l1.next.next.next.next.next.next = l1

    l4 = sol.hasCycle(l1)
    print(l4)
    # print(l4.val)
    # print(l4.next.val)
    # print(l4.next.next.val)
    # print(l4.next.next.next.val)
    # print(l4.next.next.next.next.val)
    # print(l4.next.next.next.next.next.val)