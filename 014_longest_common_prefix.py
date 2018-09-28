class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        end = self.twoprefix(strs[0], strs[1])
        for i in range(1, len(strs)):
            if self.twoprefix(strs[0], strs[i]) < end:
                end = self.twoprefix(strs[0], strs[i])
        return strs[0][:end]

    def twoprefix(self, str1, str2):
        i = 0
        while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
            i += 1
        return i


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))
    print(sol.longestCommonPrefix(["flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
    print(sol.longestCommonPrefix(["aaa","aa","aaa"]))
    print(sol.longestCommonPrefix(['']))
    print(sol.longestCommonPrefix([]))
    print(sol.longestCommonPrefix(["ca", "a"]))

