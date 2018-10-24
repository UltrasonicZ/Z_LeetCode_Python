class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) <= 1:
            return [nums]
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            for j in self.permute(nums[1:]):
                res.append([nums[0]] + j)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))
    # print(sol.permute([1, 2, 3]))
    # print(sol.permute([1, 2, 3]))
