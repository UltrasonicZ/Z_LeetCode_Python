class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] >= target:
                return i
        return i+1

if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.searchInsert([1, 3, 5, 6], 7))
    print(sol.searchInsert([1, 3, 5, 6], 0))
    # print(sol.searchInsert("aaa", "aaaa"))
    # print(sol.removeElement(1994))
