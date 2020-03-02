class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        //left/right
        int len = matrix.size();
        for (int i = 0; i<len/2; i++) {
            matrix[i].swap(matrix[len-1-i]);
        }
        for (int i = 0; i < len ; i++) {
            for (int j = i; j < len; j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        }
    }
};
