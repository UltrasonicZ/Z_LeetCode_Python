class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums_sorted = sorted(nums)
        # i = 0
        # while i+1 < len(nums):
        #     if nums_sorted[i] == nums_sorted[i+1]:
        #         pass
        #     else:
        #         return nums_sorted[i]
        #     i += 2
        # return nums_sorted[i]
        nums_sorted = sorted(nums)
        for i in range(0, len(nums), 2):
            if i+1 >= len(nums):
                break
            if nums_sorted[i] == nums_sorted[i+1]:
                pass
            else:
                return nums_sorted[i]
        return nums_sorted[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))
    print(sol.singleNumber([4, 1, 2, 1, 2]))
    print(sol.singleNumber([1, 1, 2, 3, 3]))
    # print(sol.singleNumber([2, 1]))
    # print(sol.singleNumber([-2, -1]))