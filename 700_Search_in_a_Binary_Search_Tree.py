# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # if root is None:
        #     return None
        # if root.val == val:
        #     return root
        # self.searchBST(root.left, val)
        # self.searchBST(root.right, val)
        stack = [root]
        while len(stack) > 0:
            if root.val == val:
                return root
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            root = stack.pop()

    def makeBinaryTree(self, nums, index, n):
        if index >= n or nums[index] is None:
            return
        root = TreeNode(0)
        root.val = nums[index]
        root.left = self.makeBinaryTree(nums, 2 * index + 1, n)
        root.right = self.makeBinaryTree(nums, 2 * index + 2, n)
        return root


if __name__ == "__main__":
    sol = Solution()
    a = [3, 2, 3, None, 3, None, 1]
    root = sol.makeBinaryTree(a, 0, len(a))
    print(sol.searchBST(root, 2))
    a = [3, 4, 5, 1, 3, None, 1]
    root = sol.makeBinaryTree(a, 0, len(a))
    print(sol.searchBST(root, 5))
