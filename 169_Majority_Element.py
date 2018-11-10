class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Limit Exceeded1
        # majority_count = len(nums) / 2
        # for num in nums:
        #     count = 0
        #     for elem in nums:
        #         if elem == num:
        #             count += 1
        #             if count > majority_count:
        #                 return num

        # Time Limit Exceeded2
        # majority_count = len(nums) // 2
        # for num in nums:
        #     count = sum(1 for elem in nums if elem == num)
        #     if count > majority_count:
        #         return num
        nums.sort()
        return nums[len(nums)//2]


if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([3, 2, 3]))
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(sol.majorityElement([8, 8, 7, 7, 7]))