class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # count = 0
        # list_a = []
        # for i in range(len(nums)):
        #     count += nums[i] == 0
        #
        # for i in range(len(nums)):
        #     if nums[i]:
        #         list_a.append(nums[i])
        # for i in range(count):
        #     list_a.append(0)
        # for i in range(len(nums)):
        #     nums[i] = list_a[i]
        # return nums

        count = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[count] = nums[i]
                count += 1
        for i in range(count, len(nums)):
            nums[i] = 0
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0,1,0,3,12]))