# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        right = self.get_depth(root.right)
        left = self.get_depth(root.left)
        if abs(right - left) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)

    def get_depth(self, root):
        if not root:
            return 0
        right = self.get_depth(root.right)
        left = self.get_depth(root.left)
        return max(left, right) + 1


if __name__ == "__main__":
    sol = Solution()
    l1 = TreeNode(3)
    l1.left = TreeNode(9)
    l1.right = TreeNode(20)
    l1.right.left = TreeNode(15)
    l1.right.right = TreeNode(7)
    print(sol.isBalanced(l1))