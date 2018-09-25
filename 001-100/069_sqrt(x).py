class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # use the package
        # import math
        # print(math.floor(math.sqrt(x)))

        # Time Limit Exceeded
        # i = 0
        # while i ** 2 < x:
        #     i += 1
        # if i ** 2 > x:
        #     i -= 1
        # return i

        # binary search
        l, r = 1, x
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            if mid ** 2 > x:
                r = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
            else:
                return mid
        return mid


if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(0))
    print(sol.mySqrt(3))
    print(sol.mySqrt(9))
    print(sol.mySqrt(8))