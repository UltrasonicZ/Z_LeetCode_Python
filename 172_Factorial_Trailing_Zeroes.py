class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = 0
        # i = 5
        # while n // i > 0:
        #     res += n // i
        #     i *= 5
        # return res
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.trailingZeroes(3))
    print(sol.trailingZeroes(5))
    print(sol.trailingZeroes(25))