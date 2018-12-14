class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -2, -1):
            if nums[i] < nums[i + 1]:
                break
        if i < 0:
            nums.reverse()
        # elif i == len(nums) - 2:
        #     nums[len(nums) - 2], nums[len(nums) - 1] = nums[len(nums) - 1], nums[len(nums) - 2]
        else:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    break
            nums[j], nums[i] = nums[i], nums[j]
            self.nums_reverse(nums, i + 1, len(nums) - 1)
        return nums

    def nums_reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.nextPermutation([1, 2, 4, 6, 2]))
    print(sol.nextPermutation([4, 6, 5, 1]))
    print(sol.nextPermutation([5, 1]))
    print(sol.nextPermutation([1]))
    print(sol.nextPermutation([1, 2, 3, 4]))
    print(sol.nextPermutation([3, 2, 1]))
    print(sol.nextPermutation([1, 1, 5]))
