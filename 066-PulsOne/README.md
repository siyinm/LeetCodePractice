Given a **non-empty** array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

### Solution

用数组模拟加法

一个循环，分类讨论是否为9（是否需要进位）即可