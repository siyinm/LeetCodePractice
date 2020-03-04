Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:
```

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

### Solution

动态规划：

储存当前位置最大值，每一步更新全局最大值

在原地修改储存，不占用额外空间。

规律：

我们可以从第一个正数开始算起,每往后加一个数便更新一次和的最大值;

当当前和成为负数时,则表明此前序列无法为后面提供最大子序列和,因此必须重新确定序列首项.

