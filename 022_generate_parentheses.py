class Solution(object):
    def generateParenthesis(self, N):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(mstr, l, r):
            if l == 0 and r == 0:
                res.append(mstr)
            if l > 0:
                helper(mstr + '(', l - 1, r)
            if r > 0 and r > l:
                helper(mstr + ')', l, r - 1)

        res = []
        helper('', N, N)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))
    # print(sol.isValid("()[]{}"))
    # print(sol.isValid("(]"))