class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp_1 = 1
        dp_2 = 2
        dp = 0
        for i in range(2, n):
            dp = dp_1 + dp_2
            dp_1 = dp_2
            dp_2 = dp
        return dp

        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(4))
    print(sol.climbStairs(5))

    print(sol.climbStairs(6))

    print(sol.climbStairs(7))

    print(sol.climbStairs(8))

    print(sol.climbStairs(9))

    print(sol.climbStairs(10))

    print(sol.climbStairs(11))
    print(sol.climbStairs(15))