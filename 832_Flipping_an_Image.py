class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # for i in range(len(A)):
        #     A[i].reverse()
        # for i in range(len(A)):
        #     for j in range(len(A[0])):
        #         A[i][j] = 1 - A[i][j]
        # return A
        return [[1-i for i in row[::-1]] for row in A]

        # return [[1 - i for i in row[::-1]] for row in A]


if __name__ == "__main__":
    sol = Solution()
    print(sol.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
    print(sol.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
    # print(sol.flipAndInvertImage("UDLR"))