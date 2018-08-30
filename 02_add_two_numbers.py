class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    add = 0
    l3 = ListNode(0)
    cur = l3
    while l1 or l2:
        l1_temp = 0
        l2_temp = 0
        if l1:
            l1_temp = l1.val
            l1 = l1.next
        if l2:
            l2_temp = l2.val
            l2 = l2.next
        sum = l1_temp + l2_temp + add
        if sum >= 10:
            cur.val = sum % 10
            add = 1
        else:
            cur.val = sum
            add = 0
        if l1 or l2 or add:
            if add:
                cur.next = ListNode(1)
            else:
                cur.next = ListNode(0)
            cur = cur.next
    return l3


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(1)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    l3 = addTwoNumbers(l1, l2)
    print(l3.val)
    print(l3.next.val)
    print(l3.next.next.val)
    # print(l3.next.next.next.val)
    # print(l3.next.next.next.next.val)

