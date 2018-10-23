class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newTail = 0
        for i in range(1, len(nums)):
            if nums[newTail] != nums[i]:
                newTail += 1
                nums[newTail] = nums[i]
        return newTail + 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1, 1, 2]))
    print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))