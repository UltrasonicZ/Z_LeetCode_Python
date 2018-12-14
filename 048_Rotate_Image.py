class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix) - 1
        for j in range(len(matrix) // 2):
            for i in range(n - 2 * j):
                matrix[j][i + j], matrix[n - i - j][j] = \
                    matrix[n - i - j][j], matrix[j][i + j]
                matrix[n - i - j][j], matrix[n - j][n - i - j] = \
                    matrix[n - j][n - i - j], matrix[n - i - j][j]
                matrix[n - j][n - i - j], matrix[i + j][n - j] = \
                    matrix[i + j][n - j], matrix[n - j][n - i - j]



        # for i in range(len(matrix) - 1):
        #     matrix[0][i], matrix[n - i][0] = \
        #         matrix[n - i][0], matrix[0][i]
        #     matrix[n - i][0], matrix[n][n - i] = \
        #         matrix[n][n - i], matrix[n - i][0]
        #     matrix[n][n - i], matrix[i][n] = \
        #         matrix[i][n], matrix[n][n - i]
        return matrix


if __name__ == "__main__":
    sol = Solution()
    print(sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sol.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]))
    # print(sol.rotate([1, 2, 3]))
