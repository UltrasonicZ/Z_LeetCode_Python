# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        num = len(lists) // 2
        left = self.mergeKLists(lists[:num])
        right = self.mergeKLists(lists[num:])
        return self.merge2lists(left, right)

    def merge2lists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        l3 = ListNode(0)
        cur = l3
        while l1 and l2:
            if l1.val < l2.val:
                cur.val = l1.val
                l1 = l1.next
            else:
                cur.val = l2.val
                l2 = l2.next
            cur.next = ListNode(0)
            cur = cur.next

        while l1:
            cur.val = l1.val
            if l1.next != None:
                cur.next = ListNode(0)
                cur = cur.next
            l1 = l1.next
        while l2:
            cur.val = l2.val
            if l2.next != None:
                cur.next = ListNode(0)
                cur = cur.next
            l2 = l2.next
        return l3


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    # l1.next.next.next = ListNode(1)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)
    # l2.next.next = ListNode(4)

    l4 = sol.mergeKLists([l1, l2, l3])
    print(l4.val)
    print(l4.next.val)
    print(l4.next.next.val)
    print(l4.next.next.next.val)
    print(l4.next.next.next.next.val)
    print(l4.next.next.next.next.next.val)
    print(l4.next.next.next.next.next.next.val)
    print(l4.next.next.next.next.next.next.next.val)