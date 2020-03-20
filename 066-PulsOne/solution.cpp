class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int flag = 1;
        for (int i = digits.size()-1;i>=0;i--){
            if (digits[i]!= 9 && flag) {
                digits[i]+=1;
                flag = 0;
                break;
            }
            if (digits[i] == 9 && flag){
                digits[i] = 0;
            }
        }
        if (flag == 1) digits.insert(digits.begin(), 1);
        return digits;
    }
};
