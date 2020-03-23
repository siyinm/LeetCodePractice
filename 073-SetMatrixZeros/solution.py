class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = []
        row = []
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    col.append(j)
                    row.append(i)
        for i in range(rows):    
            if i in row:
                matrix[i] = [0 for _ in range(cols)]
        for j in range(cols):
            if j in col:
                for _ in range(rows):
                    matrix[_][j] = 0
        return matrix
