class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        a, b, temp = nums[0], max(nums[0], nums[1]), 0
        for i in range(2, n):
            temp = max(a + nums[i], b)
            a = b
            b = temp
        return temp


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 7, 9, 3, 1]))
    print(sol.rob([1, 6, 3, 4, 5]))
