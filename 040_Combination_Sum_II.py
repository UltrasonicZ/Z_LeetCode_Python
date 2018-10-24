class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates, target, index, path, res):
            if target == 0 and path not in res:
                return res.append(path)
            elif target < 0:
                return False
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    break
                dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(sol.combinationSum2([2, 5, 2, 1, 2], 5))