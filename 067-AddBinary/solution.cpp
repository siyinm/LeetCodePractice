class Solution {
public:
    string addBinary(string a, string b) {
        int carry = 0;
        int i = a.length()-1;
        int j = b.length()-1;
        string ans;
        while (i >= 0 || j >=0 || carry > 0){
            int fi = a[i] - '0';
            int se = b[j] - '0';
            int sum = fi + se + carry;
            cout<<sum<<endl;
            if (sum == 0) {
                ans += '0';
                carry = 0;
            }
            else if (sum == 1) {
                ans += '1';
                carry = 0;
            }
            else if (sum == 2) {
                ans += '0';
                carry = 1;
            }
            else if (sum == 3) {
                ans += '1';
                carry = 1;
            } 
            if (i == 0 && (carry != 0 || j != 0)) {
                a[i] = '0';
                i++;
            }
            if (j == 0 && (carry != 0|| i != 0)) {
                b[j] = '0';
                j++;
            }
            i--;
            j--;
        }
        string res;
        for (int i =ans.length()-1; i >=0;i--){
            res+=ans[i];
        }

        return res;
    }
};
