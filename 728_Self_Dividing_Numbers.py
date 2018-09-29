class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        list_num = []
        for i in range(left, right + 1):
            list_str_i = list(str(i))
            if '0' in list_str_i:
                continue
            count = 0
            for j in range(len(list_str_i)):
                if i % int(list_str_i[j]) == 0:
                    count += 1
            if count == len(list_str_i):
                list_num.append(i)
        return list_num


if __name__ == "__main__":
    sol = Solution()
    print(sol.selfDividingNumbers(1, 22))
    print(sol.selfDividingNumbers(1, 2))