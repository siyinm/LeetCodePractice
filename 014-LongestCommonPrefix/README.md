## Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

```{}
Input: ["flower","flow","flight"]
Output: "fl"
```

### Solution

1. 水平扫描： 初始化res为list第一项第一位，比较list中每一个string第i位的值是否相同，不同返回当前res值

2. 初始化第一个字符串作为res，然后依次与每一个字符串比较更新res，若某一趟途中res为空，直接返回即可，这样，最后得到的res即为所求。
3. 二分查找，字典树等也可行

