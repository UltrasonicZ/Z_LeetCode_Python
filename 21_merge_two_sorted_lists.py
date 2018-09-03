# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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
    l1 = ListNode(2)
    l1.next = ListNode(3)
    l1.next.next = ListNode(6)
    # l1.next.next.next = ListNode(1)

    l2 = ListNode(1)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)

    l3 = sol.mergeTwoLists(l1, l2)
    print(l3.val)
    print(l3.next.val)
    print(l3.next.next.val)
    print(l3.next.next.next.val)
    print(l3.next.next.next.next.val)
    print(l3.next.next.next.next.next.val)
    # print(l3.next.next.next.next.next.next.val)
    # print(l3.next.next.next.next.next.next.next.val)


# if __name__ == "__main__":
#     sol = Solution()
#     # print(sol.intToRoman("III"))
#     print(sol.mergeTwoLists(3))
#     print(sol.mergeTwoLists(4))
#     print(sol.intToRoman(9))
#     print(sol.intToRoman(58))
#     print(sol.intToRoman(1994))
