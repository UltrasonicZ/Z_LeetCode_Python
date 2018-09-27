class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        dict_words = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        list_b = []
        for i in range(len(words)):
            list_a = []
            for j in range(len(words[i])):
                num = ord(words[i][j]) - ord('a')
                list_a.append(dict_words[num])
            list_b.append("".join(list_a))
        return len(set(list_b))


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
    # print(sol.uniqueMorseRepresentations("I"))
    # print(sol.uniqueMorseRepresentations("DI"))