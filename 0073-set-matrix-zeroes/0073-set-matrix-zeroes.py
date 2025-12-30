class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        total_rows = len(matrix)
        total_columns = len(matrix[0])

        rows_with_zero = set()
        columns_with_zero = set()

        for row_index in range(total_rows):
            for column_index in range(total_columns):
                if matrix[row_index][column_index] == 0:
                    rows_with_zero.add(row_index)
                    columns_with_zero.add(column_index)

        for row_index in range(total_rows):
            for column_index in range(total_columns):
                if row_index in rows_with_zero or column_index in columns_with_zero:
                    matrix[row_index][column_index] = 0
