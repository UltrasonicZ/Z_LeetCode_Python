class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return "%.5f" % x ** n
        return x ** n


if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.00000, 10))
    print(sol.myPow(2.10000, 3))
    print(sol.myPow(2.00000, -2))