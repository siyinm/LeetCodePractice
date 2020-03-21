You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
```

### Solution

本问题其实常规解法可以分成多个子问题，爬第n阶楼梯的方法数量，等于 2 部分之和

1.  爬上 n−1 阶楼梯的方法数量。因为再爬1阶就能到第n阶
2. 爬上 n−2 阶楼梯的方法数量，因为再爬2阶就能到第n阶

所以我们得到公式 $d p[n]=d p[n-1]+d p[n-2]$

同时需要初始化$d p[0]=1$ 和  $d p[1]=1$

时间复杂度：O(n)

