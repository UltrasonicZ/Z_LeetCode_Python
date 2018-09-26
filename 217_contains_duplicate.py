class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([5, 2, 6, 1]))
    print(sol.containsDuplicate([1, 2, 3, 1]))
    print(sol.containsDuplicate([1, 2, 3, 4]))
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
    print(sol.containsDuplicate([1]))