class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        str_b = list(s)
        len_a = len(s)
        str_a = str_b.copy()
        str_b.reverse()
        c = [[0 for i in range(len_a+1)] for j in range(len_a+1)]
        s_max = 0
        end = 0
        # for i in range(len_a):
        #     for j in range(len_a):
        #         if str_a[i] == str_b[j]:
        #             c[i+1][j+1] = c[i][j] + 1
        #             if c[i+1][j+1] > s_max:
        #                 str_c = str_a[i+1 - c[i+1][j+1]: i+1]
        #                 if str_c == str_c[::-1]:
        #                     s_max = c[i+1][j+1]
        #                     end = i + 1
        # return "".join(str_a[end-s_max:end])
        for i in range(len_a):
            for j in range(len_a):
                if str_a[i] == str_b[j]:
                    c[i+1][j+1] = c[i][j] + 1
                    if c[i+1][j+1] > s_max:
                        s_max = c[i+1][j+1]
                        end = i + 1
        return "".join(str_a[end-s_max:end])


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd"))
    print(sol.longestPalindrome('cbbd'))

    print(sol.longestPalindrome('abacdfgdcaba'))

