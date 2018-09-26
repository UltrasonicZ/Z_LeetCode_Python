class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] in t:
                del t[t.index(s[i])]
        return t[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.findTheDifference("abcd", "abcde"))
    print(sol.findTheDifference("a", "aa"))
    # print(sol.getSum(1, 7))
    # print(sol.getSum(1, 8))
    # print(sol.getSum(1, 5))