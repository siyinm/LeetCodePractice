A message containing letters from A-Z is being encoded to numbers using the following mapping:

```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```


Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

```
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```


Example 2:

```
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

### Solution

动态规划

如果当前位为0：

- 如果前一位不是1或2，则无法组成字母，整个串无法构成编码
- 如果前一位是1或者2，这时候构成的编码数目和之前相同的，因为只存在"10"或"20"的解码，即：dp[i] = dp[i-2]

如果当前位不为0：

- 如果前一位和当前位能组成字母，则编码数目应该为前一位和前两位之和，即：dp[i] = dp[i-1] + dp[i-2]
- 如果前一位和当前位不能组成字母，则当前位单独组成字母，即dp[i] = dp[i-1]