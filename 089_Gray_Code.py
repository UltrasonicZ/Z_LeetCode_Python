class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # results = [0]
        # for i in range(n):
        #     results += [x + pow(2, i) for x in reversed(results)]
        # return results
        if not n:
            return [0]
        res = [0, 1]
        for i in range(n - 1):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | 1 << (i + 1))
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.grayCode(2))
    print(sol.grayCode(3))
    print(sol.grayCode(4))