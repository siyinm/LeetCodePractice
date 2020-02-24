Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

### Solution

hash map 的思想：对row col box 分别使用三个hash map，tag 是1-9的数字，val是出现的位置（第几row, col, box), 填充，判断

采用二维数组代替了hash map，新建三个 9*10的数组（10为了方便数字入库），1为出现，0为未出现，与hash map等价