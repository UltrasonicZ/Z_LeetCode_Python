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

# class Solution:
#     # @param num, a list of integer
#     # @return a list of lists of integers
#     def permute(self, num):
#         if len(num) == 0:
#             return []
#         if len(num) == 1:
#             return [num]
#         res = []
#         for i in range(len(num)):
#             for j in self.permute(num[:i] + num[i + 1:]):
#                 res.append([num[i]] + j)
#         return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1, 2, 3]))