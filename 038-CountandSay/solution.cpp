class Solution {
public:
    string countAndSay(int n) {
        string str,res;
        res="1";
        for(int i=1;i<n;i++){
            str=res;
            res="";
            for(int j=0;j<str.size();){
                int c=0,k=j;
                while(k<str.size()&&str[k]==str[j]){
                    k++;
                    c++;
                }
                res+=to_string(c)+str[j];
                j=k;
            }
        }
        return res;
    }
};