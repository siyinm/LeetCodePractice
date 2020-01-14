## [Longest Palindromic Substring](https://leetcode-cn.com/problems/longest-palindromic-substring/)

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

```
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
```

### Solution

- Brute Force: 

  python3: 遍历每个可能的str，判断是否是回文字符（使用[::-1]），最后输出最长的那个

  Time Complexity： $O(n^2)$

  Space Complexity：$O(1)$

- 中心扩展，遍历每个中心点，character和两个character之间 (without codes )

- b#a#b#a#d 新建数组 动态规划 (without codes )