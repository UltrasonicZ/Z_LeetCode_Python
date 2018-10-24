class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) <= 1:
            return [nums]
        for i in range(len(nums)):
            nums[0], nums[i] = nums[i], nums[0]
            for j in self.permuteUnique(nums[1:]):
                if [nums[0]] + j not in res:
                    res.append([nums[0]] + j)
        return res

        # if len(nums) == 1:
        #     return [nums]
        # res = []
        # for i in range(len(nums)):
        #     for j in self.permuteUnique(nums[:i] + nums[i + 1:]):
        #         if [nums[i]] + j not in res:
        #             res.append([nums[i]] + j)
        # return res

    # def permuteUnique(self, nums):
    #     ans = [[]]
    #     for n in nums:
    #         new_ans = []
    #         for l in ans:
    #             for i in range(len(l) + 1):
    #                 new_ans.append(l[:i] + [n] + l[i:])
    #                 if i < len(l) and l[i] == n:
    #                     break  # handles duplication
    #         ans = new_ans
    #     return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.permuteUnique([3, 1, 3, 3]))