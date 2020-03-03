Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
### Solution
递归解决
用快速幂算法

if x is even, $x^n=A*A$

if x is odd, $x^n=A * A * x$

Time/Space complexity: O(log(n))





