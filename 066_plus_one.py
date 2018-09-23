class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        return [int(i) for i in str(num + 1)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 3]))
    print(sol.plusOne([4, 3, 2, 1]))
    # print(sol.plusOne("1010", "1011"))
