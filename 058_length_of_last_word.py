class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = s.split()
        if not len(s) or not len(list_s):
            return 0
        return len(list_s[-1])

        # return len("  ".lstrip())


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World！"))
    print(sol.lengthOfLastWord('1'))
    print(sol.lengthOfLastWord('  '))
    print(sol.lengthOfLastWord('Hello  '))
