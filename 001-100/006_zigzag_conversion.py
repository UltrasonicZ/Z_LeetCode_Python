class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_a = list(s)
        len_a = len(str_a)
        cycle = (numRows - 1) * 2
        list_b = []
        for i in range(0, len_a, cycle):
            list_b.append(str_a[i])
        for i in range(1, numRows-1):
            # inter = 2*i
            j = 0
            flag = 0
            while j < len_a:
                if flag == 1:
                    j = cycle - 2*i
                    flag = 0
                else:
                    j = cycle

            for j in range(i, len_a):
                if j+cycle-i < len_a:
                    list_b.append(str_a[j+cycle-i])

        for i in range(numRows-1, len_a, cycle):
            list_b.append(str_a[i])
        return "".join(list_b)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.convert("kztakrekvefgchersuoiuatzlmwynzjhdqqftjcqmntoyckqfawikkdrnfgbwtdpbkymvwoumurjdzygyzsbmwzpcxcdmmpwzmeibligwiiqbecxwyxigikoewwrczkanwwqukszsbjukzumzladrvjefpegyicsgctdvldetuegxwihdtitqrdmygdrsweahfrepdcudvyvrggbkthztxwicyzazjyeztytwiyybqdsczozvtegodacdokczfmwqfmyuixbeeqluqcqwxpyrkpfcdosttzooykpvdykfxulttvvwnzftndvhsvpgrgdzsvfxdtzztdiswgwxzvbpsjlizlfrlgvlnwbjwbujafjaedivvgnbgwcdbzbdbprqrflfhahsvlcekeyqueyxjfetkxpapbeejoxwxlgepmxzowldsmqllpzeymakcshfzkvyykwljeltutdmrhxcbzizihzinywggzjctzasvefcxmhnusdvlderconvaisaetcdldeveeemhugipfzbhrwidcjpfrumshbdofchpgcsbkvaexfmenpsuodatxjavoszcitjewflejjmsuvyuyrkumednsfkbgvbqxfphfqeqozcnabmtedffvzwbgbzbfydiyaevoqtfmzxaujdydtjftapkpdhnbmrylcibzuqqynvnsihmyxdcrfftkuoymzoxpnashaderlosnkxbhamkkxfhwjsyehkmblhppbyspmcwuoguptliashefdklokjpggfiixozsrlwmeksmzdcvipgkwxwynzsvxnqtchgwwadqybkguscfyrbyxudzrxacoplmcqcsmkraimfwbauvytkxdnglwfuvehpxd"))
    # print(sol.convert('cbbd'))
    print(sol.convert("PAYPALISHIRING", 3))
    print(sol.convert("PAYPALISHIRING", 4))
    print(sol.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    print(sol.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")






