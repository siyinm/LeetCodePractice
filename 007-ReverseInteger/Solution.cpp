class Solution {
public:
    int reverse(int x) {
        int rev=0;
        while (x!=0){
            int pop=x%10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && rev>(INT_MAX-pop)/10)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && rev<(INT_MIN-pop)/10)) return 0;
            x/=10;
            rev=rev*10+pop;
        }
        return rev;
    }    
};
