class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        str_list = []
        str_n_1 = str(self.countAndSay(n - 1))

        look = str_n_1[0]
        say = 1
        j = 1
        while j < len(str_n_1) and str_n_1[j]:
            if look == str_n_1[j]:
                say += 1
            else:
                str_list.extend(str(say))
                str_list.extend(str(look))
                look = str_n_1[j]
                say = 1
            j += 1
        str_list.extend(str(say))
        str_list.extend(str(look))

        return "".join(str_list)


if __name__ == "__main__":
    sol = Solution()
    print(sol.countAndSay(1))
    print(sol.countAndSay(2))
    print(sol.countAndSay(3))
    print(sol.countAndSay(4))
    print(sol.countAndSay(5))
    print(sol.countAndSay(6))
    print(sol.countAndSay(7))
    print(sol.countAndSay(8))
    print(sol.countAndSay(9))
    print(sol.countAndSay(10))