class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        len_list_a = 1
        dict_digits = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                       '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                       '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        for i in range(len(digits)):
            if digits[i] == '7' or digits[i] == '9':
                len_list_a *= 4
            else:
                len_list_a *= 3
        list_a = ['' for _ in range(len_list_a)]
        len_list = len_list_a
        for i in range(len(digits)):
            values = dict_digits[digits[i]]
            len_list = len_list // len(values)
            j = 0
            k = 0
            while j < len_list_a:
                list_a[j] += values[k]
                j += 1
                if not j % len_list:
                    k += 1
                k %= len(values)
        return list_a


if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations("234"))
    print(sol.letterCombinations("27"))
