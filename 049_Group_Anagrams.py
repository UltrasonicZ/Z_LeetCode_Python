class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # from collections import defaultdict
        # dict_strs = defaultdict(list)
        dict_strs = {}
        for w in strs:
            key = "".join(sorted(w))
            # dict_strs[key].append(w)
            dict_strs.setdefault(key, []).append(w)
        return list(dict_strs.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))