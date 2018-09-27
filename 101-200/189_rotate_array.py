class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # while k:
        #     tmp = nums[-1]
        #     for i in range(len(nums) - 1, 0, -1):
        #         nums[i] = nums[i - 1]
        #     nums[0] = tmp
        #     k -= 1
        # return nums

        k = k % len(nums)
        nums_b = [0 for _ in range(k)]
        for i in range(k):
            nums_b[i] = nums[len(nums) - k + i]
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]
        for i in range(k):
            nums[i] = nums_b[i]
        return nums

        # k = k % len(nums)
        # nums_cp = nums.copy()
        # for i in range(len(nums)):
        #     nums[(i + k) % len(nums)] = nums_cp[i]
        # return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([1, 2, 3, 4, 5, 6, 7], 3))