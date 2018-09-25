# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        last = cur
        cur = cur.next
        while cur:
            if cur.val == last.val:
                # last.next = cur.next
                # cur = last.next
                cur = cur.next
                last.next = cur
            else:
                cur = cur.next
                last = last.next
        return head


if __name__ == "__main__":
    sol = Solution()

    # l1 = ListNode(1)
    # l1.next = ListNode(1)
    # l1.next.next = ListNode(2)
    # l1.next.next.next = ListNode(3)
    # l1.next.next.next.next = ListNode(3)

    l2 = ListNode(1)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)

    l3 = sol.deleteDuplicates(l2)
    print(l3.val)
    print(l3.next.val)
    # print(l3.next.next.val)
    # print(l3.next.next.next.val)
    # print(l3.next.next.next.next.val)
    # print(l3.next.next.next.next.next.val)
    # print(l3.next.next.next.next.next.next.val)
    # print(l3.next.next.next.next.next.next.next.val)
