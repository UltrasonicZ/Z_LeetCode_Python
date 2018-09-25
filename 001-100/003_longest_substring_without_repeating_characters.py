class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        list_a = []
        list_b = []
        s = list(s)
        # count = [1] * len(one_str)
        for i in range(len(s)):
            tmp = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in tmp:
                    tmp += s[j]
                else:
                    break
            list_a.append(len(tmp))
        return max(list_a, default=0)


if __name__ == "__main__":

    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))

    print(sol.lengthOfLongestSubstring('bbbbbb'))

    print(sol.lengthOfLongestSubstring('1234561789'))
