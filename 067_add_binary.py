class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = list(a)
        a.reverse()
        b = list(b)
        b.reverse()
        i = 0
        add = 0
        num = [0 for _ in range(max(len(a), len(b)) + 1)]
        while i < len(a) and i < len(b):
            a_num = int(a[i])
            b_num = int(b[i])
            num[i] = str((a_num + b_num + add) % 2)
            if a_num + b_num + add > 1:
                add = 1
            else:
                add = 0
            i += 1
        j = i-1
        for j in range(i, len(a)):
            a_num = int(a[j])
            num[j] = str((a_num + add) % 2)
            if a_num + add > 1:
                add = 1
            else:
                add = 0
        for j in range(i, len(b)):
            b_num = int(b[j])
            num[j] = str((b_num + add) % 2)
            if b_num + add > 1:
                add = 1
            else:
                add = 0
        if add:
            num[j+1] = '1'
        else:
            del num[j+1]
        return "".join(num[::-1])


if __name__ == "__main__":
    sol = Solution()
    print(sol.addBinary("11", "1"))
    print(sol.addBinary("101", "10"))
    print(sol.addBinary("1010", "1011"))
    print(sol.addBinary("110011", "11"))
    print(sol.addBinary("110010", "10111"))
