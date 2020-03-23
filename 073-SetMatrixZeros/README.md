Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

```
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

### Solution

常数额外空间

第一遍循环找0，分别储存row and col

第二遍循环置换row

第三遍循环置换col