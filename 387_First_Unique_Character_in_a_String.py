class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in s[i + 1: len(s)] and s[i] not in s[0: i]:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUniqChar("leetcode"))
    print(sol.firstUniqChar("loveleetcode"))
    print(sol.firstUniqChar("e"))
    print(sol.firstUniqChar(""))
    print(sol.firstUniqChar("cc"))
    print(sol.firstUniqChar("aadadaad"))
