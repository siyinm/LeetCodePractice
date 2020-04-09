Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```

### Solution

动态规划

和替换字母那道差不多，对于字符串的匹配问题，最好使用d p，效率高于思想为遍历的dfs等搜索策略

- `dp[i][j]`用来表示`s1`的前i项和`s2`的前j项能不能构成`s3`的前`i+j`项
- 判断方法：看`dp[i-1][j]`和`dp[i][j-1]`以及下一项和s3的匹配情况
- 判断最后一格子即可



主要是如何使用dp 记录每一步之前的情况，二维表格最直观

