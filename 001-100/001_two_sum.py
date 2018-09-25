class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         a = target - nums[i]
        #         b = nums[j]
        #         if a != b:
        #             continue
        #         else:
        #             return [i, j]
        nums_cp = nums.copy()
        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [nums[i], nums[j]]


if __name__ == "__main__":
    # nums_in = input()
    # target = int(input())
    # numbers = nums_in.split()
    # # print(numbers)
    # nums = [0] * len(numbers)
    # for i in range(len(numbers)):
    #     nums[i] = int(numbers[i])
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))
    print(sol.twoSum([3, 2, 4], 6))
    print(sol.twoSum([3, 3], 6))
