class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, index, path, res):
            if target == 0:
                return res.append(path)
            elif target < 0:
                return False
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res

        # res = []
        # if len(nums) <= 1:
        #     return [nums]
        # for i in range(len(nums)):
        #     nums[0], nums[i] = nums[i], nums[0]
        #     for j in self.permute(nums[1:]):
        #         res.append([nums[0]] + j)
        # return res

    # def combinationSum(self, candidates, target):
    #     res = []
    #     candidates.sort()
    #     self.dfs(candidates, target, 0, [], res)
    #     return res
    #
    # def dfs(self, nums, target, index, path, res):
    #     if target < 0:
    #         return  # backtracking
    #     if target == 0:
    #         res.append(path)
    #         return
    #     for i in range(index, len(nums)):
    #         self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
    print(sol.combinationSum([2, 3, 5], 8))