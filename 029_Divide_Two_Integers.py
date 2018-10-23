class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i += i
                temp += temp
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

        # positive = (dividend < 0) is (divisor < 0)
        # dividend, divisor = abs(dividend), abs(divisor)
        # res = 0
        # while dividend >= divisor:
        #     temp, i = divisor, 1
        #     while dividend >= temp:
        #         res += i
        #         dividend -= temp
        #         temp <<= 1
        #         i <<= 1
        # if not positive:
        #     res = -res
        # return max(min(2147483647, res), -2147483648)


if __name__ == "__main__":
    sol = Solution()
    print(sol.divide(10, 3))
    print(sol.divide(7, -3))