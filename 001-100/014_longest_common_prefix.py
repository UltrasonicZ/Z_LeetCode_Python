class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        str_a = strs[0]
        for i in range(1, len(strs)):
            str_a = self.DP_LCS(str_a, strs[i])
        return str_a

    def DP_LCS(self, str1, str2):
        max_str = 0
        end = 0
        c = [[0 for _ in range(len(str2)+1)]for _ in range(len(str1)+1)]
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    c[i+1][j+1] = c[i][j] + 1
                    max_str = c[i+1][j+1]
                    end = i
                elif c[i][j+1] >= c[i+1][j]:
                    c[i+1][j+1] = c[i][j+1]
                else:
                    c[i+1][j+1] = c[i+1][j]
        return str1[end+1-max_str: end+1]


if __name__ == "__main__":
    sol = Solution()
    # print(sol.longestCommonPrefix(["flower","flow","flight"]))
    # print(sol.longestCommonPrefix(["flow", "flight"]))
    # print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
    # print(sol.longestCommonPrefix(["aaa","aa","aaa"]))
    # print(sol.longestCommonPrefix(['']))
    # print(sol.longestCommonPrefix([]))
    print(sol.longestCommonPrefix(["ca", "a"]))

