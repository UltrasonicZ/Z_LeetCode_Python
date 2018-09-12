class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.intToRoman("III"))
    print(sol.removeElement([3, 2, 2, 3], 3))
    print(sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
    # print(sol.removeElement(9))
    # print(sol.removeElement(58))
    # print(sol.removeElement(1994))


