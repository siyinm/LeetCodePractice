## Longest substring without repeating characters

### Discription

Given a string, find the length of the longest substring without repeating characters.

### Example

Example1:

```{cpp}
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3.   
```

Example 2:

```{cpp}
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```


Example 3:

```{cpp}
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

### Solution

- 使用左右两指针，```int left, right```， 大循环移动右侧指针， 小循环遍历两指针之间的值， 若```s[i]```与```right+1``` 相同， 则左指针移动到相同项的右边一位，即```s[i+1]``` ，
- sliding window: 滑动窗口