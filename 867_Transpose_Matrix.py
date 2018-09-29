class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        num_row, num_col = len(A), len(A[0])
        B = [[0 for _ in range(num_row)] for _ in range(num_col)]
        for i in range(num_row):
            for j in range(num_col):
                B[j][i] = A[i][j]
        return B


if __name__ == "__main__":
    sol = Solution()
    print(sol.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sol.transpose([[1, 2, 3], [4, 5, 6]]))