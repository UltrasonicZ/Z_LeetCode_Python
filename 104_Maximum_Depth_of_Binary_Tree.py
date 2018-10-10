# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        right = self.maxDepth(root.right)
        left = self.maxDepth(root.left)
        return max(left, right) + 1


if __name__ == "__main__":
    sol = Solution()
    l1 = TreeNode(3)
    l1.left = TreeNode(9)
    l1.right = TreeNode(20)
    l1.right.left = TreeNode(15)
    l1.right.right = TreeNode(7)
    print(sol.get_depth(l1))