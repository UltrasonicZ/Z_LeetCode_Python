# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1
        k = k % count
        p.next = head
        i = 0
        while i < count - k:
            p = p.next
            i += 1
        head = p.next
        p.next = None
        return head


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)

    l4 = sol.rotateRight(l1, 2)
    # print(l4)
    print(l4.val)
    print(l4.next.val)
    print(l4.next.next.val)
    print(l4.next.next.next.val)
    print(l4.next.next.next.next.val)
    # print(l4.next.next.next.next.next.val)