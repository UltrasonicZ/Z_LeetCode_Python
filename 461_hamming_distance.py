class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return list(bin(x ^ y))[2:].count('1')


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingDistance(1, 4))
    print(sol.hammingDistance(1, 2))
    print(sol.hammingDistance(3, 7))