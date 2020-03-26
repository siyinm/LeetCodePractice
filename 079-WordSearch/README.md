Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
### Solution
回溯法
注意不能重复使用characters, set the board[i][j]=''在dfs之前，然后再traceback
