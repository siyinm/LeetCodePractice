class Solution {
public:
    int row[9][10];
    int col[9][10];
    int box[9][10];
    bool flag = false;
    void solveSudoku(vector<vector<char>>& board) { 
        for(int i=0; i<9; i++){
            for(int j = 0; j<9; j++){
                if(board[i][j] == '.') continue;
                int curNumber = board[i][j]-'0';
                row[i][curNumber] = 1;
                col[j][curNumber] = 1;
                box[j/3 + (i/3)*3][curNumber] = 1;
            }
        }
        dfs(board, 0);
    }
    void dfs(vector<vector<char>>& board, int index){
        if (index >= 81 ){
            flag = true;
            return;
        }
        int r = index/9;
        int c = index%9;
        if (board[r][c]!='.'){
            dfs(board, index+1);
            return; 
        }
        for (int i = 1; i<=9 ; i++){
            if (row[r][i] || col[c][i] || box[r/3*3+c/3][i]) continue;
            row[r][i] = 1;
            col[c][i] = 1;
            box[r/3*3+c/3][i] = 1;
            board[r][c] = '0'+i;
            dfs(board, index+1);
            if (flag) return;
            row[r][i] = 0;
            col[c][i] = 0;
            box[r/3*3+c/3][i] = 0;
            board[r][c] = '.';
        }
    }
};
