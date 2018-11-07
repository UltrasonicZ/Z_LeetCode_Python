# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # for recursion
    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     l, r = 0, 0
    #     return self.helper(root, l, r)
    #
    # def helper(self, root, l, r):
    #     if root is None:
    #         return 0
    #     ll, lr, rl, rr = 0, 0, 0, 0
    #     if root.left:
    #         ll = self.helper(root.left.left, ll, lr)
    #     if root.left:
    #         lr = self.helper(root.left.right, ll, lr)
    #     if root.right:
    #         rl = self.helper(root.right.left, rl, rr)
    #     if root.right:
    #         rr = self.helper(root.right.right, rl, rr)
    #     l = self.helper(root.left, ll, lr)
    #     r = self.helper(root.right, rl, rr)
    #     return max(ll + lr + rl + rr + root.val, l + r)

    # for DP from top to down
    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     m = {}
    #     return self.helper(root, m)
    #
    # def helper(self, root, m):
    #     if root is None:
    #         return 0
    #     if root in m:
    #         return m[root]
    #     val = 0
    #     if root.left:
    #         val += self.helper(root.left.left, m) + self.helper(root.left.right, m)
    #     if root.right:
    #         val += self.helper(root.right.left, m) + self.helper(root.right.right, m)
    #     val = max(val + root.val, self.helper(root.left, m) + self.helper(root.right, m))
    #     m[root] = val
    #     return val

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = self.helper(root)
        return max(res[0], res[1])

    def helper(self, root):
        if root is None:
            return [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        res = [0, 0]
        res[0] = max(left[0], left[1]) + max(right[0], right[1])
        res[1] = root.val + left[0] + right[0]
        return res

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
    print(sol.rob(root))
    a = [3, 4, 5, 1, 3, None, 1]
    root = sol.makeBinaryTree(a, 0, len(a))
    print(sol.rob(root))