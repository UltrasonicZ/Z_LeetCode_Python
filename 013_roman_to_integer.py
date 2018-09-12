class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_a = list(s)
        sum_1 = 0
        dic_str = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(str_a)):
            sum_1 += dic_str[str_a[i]]
            if str_a[i] == 'V' or str_a[i] == 'X':
                if str_a[i - 1] == 'I' and i > 0:
                    sum_1 -= 2
            if str_a[i] == 'L' or str_a[i] == 'C':
                if str_a[i - 1] == 'X' and i > 0:
                    sum_1 -= 20
            if str_a[i] == 'D' or str_a[i] == 'M':
                if str_a[i - 1] == 'C' and i > 0:
                    sum_1 -= 200
        return sum_1


if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInt("III"))
    print(sol.romanToInt("IV"))
    print(sol.romanToInt("IX"))
    print(sol.romanToInt("LVIII"))
    print(sol.romanToInt("MCMXCIV"))
    print(sol.romanToInt("MMMCDXC"))
