class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sorted = sorted(nums)
        i = 0
        j = 1
        sum1 = 0
        sum2 = 0
        while i < len(nums) and j < len(nums):
            sum1 += nums_sorted[i]
            sum2 += nums_sorted[j]
            if sum1 == sum2:
                pass
            else:
                return nums_sorted[i]
            i += 2
            j += 2

        return nums_sorted[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))
    print(sol.singleNumber([4, 1, 2, 1, 2]))
    print(sol.singleNumber([1, 1, 2, 3, 3]))
    # print(sol.singleNumber([2, 1]))
    # print(sol.singleNumber([-2, -1]))