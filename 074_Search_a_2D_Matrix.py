class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        rows, columns = len(matrix), len(matrix[0])
        row, column = 0, columns - 1
        while row < rows and column >= 0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                row += 1
            else:
                column -= 1
        return False

# class Solution:
#     def searchMatrix(self, matrix, target):
#         """
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         """
#         if not matrix or target is None:
#             return False
#         rows, cols = len(matrix), len(matrix[0])
#         low, high = 0, rows * cols - 1
#
#         while low <= high:
#             mid = (low + high) // 2
#             num = matrix[mid // cols][mid % cols]
#
#             if num == target:
#                 return True
#             elif num < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        while row < rows and target >= matrix[row][0]:
            row += 1
        row -= 1
        low, high = 0, cols - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[row][mid]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.searchMatrix([[1,   3,  5,  7],
                            [10, 11, 16, 20],
                            [23, 30, 34, 50]], 16))
    print(sol.searchMatrix([[1,   3,  5,  7],
                            [10, 11, 16, 20],
                            [23, 30, 34, 50]], 512))
    print(sol.searchMatrix([], 512))
