class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) return 0;
        if (dividend==-2147483648&& divisor==-1) return 2147483647;
        if (divisor == 1) return dividend;
        if (divisor == -1) return -dividend;
        int flag=1;
        if ((dividend>0 and divisor>0)or (dividend<0 and divisor<0)) flag=1;
        else flag=-1;
        return flag* help(abs(long(dividend)), abs(long(divisor)));
    }
    int help(long a, long b){
        if (a < b) return 0;
        long tb = b; // 在后面的代码中不更新b
        long count=1;
        while((tb+tb)<=a){
            count = count + count; // 最小解翻倍
            tb = tb+tb; // 当前测试的值也翻倍
        }
        return count + help(a-tb,b);
    }
};

