# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    l1 = TreeNode(1)
    l1.left = TreeNode(2)
    l1.right = TreeNode(3)
    l2 = TreeNode(1)
    l2.left = TreeNode(2)
    l2.right = TreeNode(3)
    print(sol.isSameTree(l1, l2))
