class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        list_a = list(str.strip())
        if len(list_a) == 0:
             return 0
        sign = -1 if list_a[0] == '-' else 1
        if list_a[0] in ['+', '-']:
            del list_a[0]
        sum_str, i = 0, 0
        while i < len(list_a) \
                and ord(list_a[i]) - ord('0') >= 0 \
                and ord(list_a[i]) - ord('0') < 10:
            sum_str = sum_str*10 + (ord(list_a[i])-ord('0'))
            i += 1
        # if sign == -1:
        #     return max(-sum_str, -2**31)
        # return min(sum_str, 2**31-1)
        return max(-2**31, min(sign * sum_str, 2**31-1))


if __name__ == "__main__":
    sol = Solution()
    # print(sol.intToRoman("III"))
    print(sol.myAtoi("42"))
    print(sol.myAtoi("   -42"))
    print(sol.myAtoi("4193 with words"))
    print(sol.myAtoi("words and 987"))
    print(sol.myAtoi("-91283472332"))
    print(sol.myAtoi("+1"))
    print(sol.myAtoi("  0000000000012345678"))