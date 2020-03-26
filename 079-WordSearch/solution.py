class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if self.backtrack(board, i,j, word, m, n):
                        return True 
        return False 

    def backtrack(self, board, i, j, word, m, n):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = ''
            directions = [(-1, 0),(1, 0),(0, 1),(0, -1)]
            for direction in directions:
                new_x = i + direction[0]
                new_y = j + direction[1]
                if (0 <= new_x < n) and (0 <= new_y < m) and  self.backtrack(board, new_x, new_y, word[1:], m, n):
                    return True 
            board[i][j] = word[0]
        else:
            return False 
