Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

Note:

- Both dividend and divisor will be 32-bit signed integers.
- The divisor will never be 0.
- Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.

### Solution

一开始用了减法，超出时间限制

后来使用递归，依然超出时间限制

最后发现说是不让用乘法之类的但还是要考虑倍数：

例如11/3

不断以3, 3^2, 3^4...与11比较，找到最大的数字取余数再进行同样的操作

注意界限问题，负界限绝对值大于正界限，可以采用

1. 全用负数计算
2. long型