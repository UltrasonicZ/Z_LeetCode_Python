class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0] if len(nums) else 0
        return max(self.robber(nums, 0, len(nums) - 1), self.robber(nums, 1, len(nums)))

    def robber(self, nums, left, right):
        a, b, temp = 0, 0, 0
        for i in range(left, right):
            temp = max(a + nums[i], b)
            a = b
            b = temp
        return temp


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 3, 2]))
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([1, 2, 3, 4, 4]))
    print(sol.rob([]))