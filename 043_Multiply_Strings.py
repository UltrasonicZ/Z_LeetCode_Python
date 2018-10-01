class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # num1_int = 0
        # num2_int = 0
        # for i in range(len(num1)):
        #     num1_int = 10 * num1_int + (ord(num1[i])-ord('0'))
        # for i in range(len(num2)):
        #     num2_int = 10 * num2_int + (ord(num2[i]) - ord('0'))
        #
        # return str(num1_int * num2_int)
        # product = [0] * (len(num1) + len(num2))

        product = 0
        for i in range(len(num1)):
            helper = 0
            for j in range(len(num2)):
                helper = helper + (ord(num2[len(num2) - j - 1]) - 48) * \
                                  (ord(num1[len(num1) - i - 1]) - 48) * \
                                  (10 ** j)
            product = product + helper * (10 ** i)
        return str(product)


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("2", "3"))
    print(sol.multiply("123", "456"))
    # print(sol.multiply([1, 2, 3]))