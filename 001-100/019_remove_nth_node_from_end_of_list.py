# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node_1 = head
        count = 0
        # count is the num of nodes
        while node_1:
            node_1 = node_1.next
            count += 1
        # when count is 1, return []
        if count == 1:
            return []
        # change to from start to the end
        n = count - n
        # when remove the head
        if n == 0:
            head = head.next
            return head
        node = head
        while n - 1 > 0:
            node = node.next
            n -= 1
        p = node
        q = node.next.next
        p.next = q
        return head
        # return count, node.val


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)
    # l1.next.next = ListNode(3)
    # l1.next.next.next = ListNode(4)
    # l1.next.next.next.next = ListNode(5)

    l3 = sol.removeNthFromEnd(l1, 2)
    print(l3.val)
    # print(l3.next.val)
    # print(l3.next.next.val)
    # print(l3.next.next.next.val)
    # print(l3.next.next.next.next.val)