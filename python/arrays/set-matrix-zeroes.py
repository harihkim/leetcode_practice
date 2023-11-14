# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        # finding which rows and cols contain 0
        for row_index, row in enumerate(matrix):
            for col_index, ele in enumerate(row):
                if ele == 0:
                    rows.add(row_index)
                    cols.add(col_index)
        # setting all values of those rows to 0
        for row in rows:
             for col in range(num_cols):
                  matrix[row][col] = 0
        # setting all values of those cols to 0
        for col in cols:
             for row in range(num_rows):
                  matrix[row][col] = 0


matrix = [[1,1,1],[1,0,1],[1,1,1]]

setZeroes(matrix)
print(matrix)
