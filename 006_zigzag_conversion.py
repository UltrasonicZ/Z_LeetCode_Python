class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_a = list(s)
        str_b = ''
        rows = ['' for n in range(numRows)]
        if numRows == 1:
            return s
        curRow = 0
        goingDown = False
        for i in range(len(s)):
            rows[curRow] += str_a[i]
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        for row in rows:
            str_b += row
        return str_b


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("wxdfcf", 2))
    print(sol.convert("PAYPALISHIRING", 3))
    # print(sol.convert("PAYPALISHIRING", 4))
    # print(sol.convert("AB", 1))
    # print(sol.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."
# , 3))
    # print(sol.convert("jrqopubjguxhxdipfzwswybgfylqvjzharvrlyauuzdrcnjkphclffrkeecbpdipufhidjcxjhrnxcxmjcxohqanxdrmgzebhnlmwpmhwdvthsfqueeexgrujigskmvrzgfwvrftwapdtutpbztygnsrxajjngcomikjzsdwssznovdruypcnjulkfuzmxnafamespckjcazxdrtdgyrqscczybnvqqcqcjitlvcnvbmasidzgwraatzzwpwmfbfjkncvkelhhzjchpdnlunmppnlgjznkewwuysgefonexpmmsbaopmdgzqmkqzxuvtqvnxbslqzkglzamzpdnsjolvybwxxttqognrbaiakqllszkhfzconnmoqklpeefsnsmouwqhodsgcfohesyshmgxwtoayuvnojdjftqtwkbapriujimqwspslgvlcsaqbdbgwtbseettwdnfnbyjvpdjxyuzqxstatbzpctthoofremgfkrbcvkzvgbofthgojhdnaywpnbitoraaibednezwfpdawlohssvtqtkfvsylj"
# , 70))
