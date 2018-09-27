class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        str = list(str)
        for i in range(len(str)):
            if 64 < ord(str[i]) < 91:
                str[i] = chr(ord(str[i]) + 32)
        return "".join(str)


if __name__ == "__main__":
    sol = Solution()
    print(sol.toLowerCase("Hello"))
    print(sol.toLowerCase("here"))
    print(sol.toLowerCase("LOVELY"))