class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int left=0;
        int right=0;
        int length=0;
        while (right<s.length()){
            for (int i=left; i<=right; i++){
                if (s[i]==s[right+1]){
                    if (right-left+1>length){
                        length=right-left+1;
                    }
                    left=i+1;
                }
            }
            if (right-left+1>length){
                length=right-left+1;
            }
            right++;                     
        }
        return length;                         
    }                           
};
