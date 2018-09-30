# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ans = []
        self.inorder(root, ans)
        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]:
                return False
        return True

    def inorder(self, x, ans):
        if x:
            self.inorder(x.left, ans)
            ans.append(x.val)
            self.inorder(x.right, ans)


if __name__ == "__main__":
    sol = Solution()
    l1 = TreeNode(1)
    l1.left = TreeNode(3)
    l1.left.right = TreeNode(2)
    l2 = TreeNode(5)
    l2.left = TreeNode(1)
    l2.right = TreeNode(4)
    l2.right.left = TreeNode(4)
    l2.right.right = TreeNode(6)
    print(sol.isValidBST(l2))