class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # list_haystack = list(haystack)
        # list_needle = list(needle)
        # if needle == '':
        #     return 0
        # elif len(haystack) < len(list_needle):
        #     return -1
        # else:
        #     for i in range(len(list_haystack)-len(list_needle)+1):
        #         if list_haystack[i:i+len(list_needle)] == list_needle:
        #             return i
        #         flag = i
        #     if list_haystack[flag:flag+len(list_needle)] != list_needle:
        #         return -1
        len_haystack = len(haystack)
        len_needle = len(needle)
        if needle == '':
            return 0
        for i in range(len_haystack - len_needle + 1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1

if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("hello", "ll"))
    print(sol.strStr("aaaaa", "bba"))
    print(sol.strStr("hello", ""))
    print(sol.strStr("", "a"))
    print(sol.strStr("aaa", "aaaa"))
    # print(sol.removeElement(1994))
