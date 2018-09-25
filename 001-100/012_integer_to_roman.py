class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str_a = []
        dic_str = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9],
                   ['X', 10], ['XL', 40], ['L', 50], ['XC', 90],
                   ['C', 100], ['CD', 400], ['D', 500],
                   ['CM', 900], ['M', 1000]]
        i = 12
        while num >= 0 and i >= 0:
            while num >= dic_str[i][1]:
                str_a += dic_str[i][0]
                num -= dic_str[i][1]
            i -= 1
        return "".join(str_a)


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3))# "III"
    print(sol.intToRoman(4))# "IV"
    print(sol.intToRoman(9))# "IX"
    print(sol.intToRoman(58))# "LVIII"
    print(sol.intToRoman(1994))# "MCMXCIV"
    print(sol.intToRoman(3490))# "MMMCDXC"
