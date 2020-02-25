Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

## Solution
回溯问题的应用

```python
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return  
for 选择 in 选择列表:
  	(剪枝)
    做选择
    backtrack(路径, 选择列表)
    撤销选择
```

其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」

这道问题的要点在于：

- return的时机

  由于只有一个答案，建立一个flag来结束递归，i. e. 找到答案就返回，在满足结束条件后使```flag = 1```,  and judge that in the for loop before we 撤销选择.

  
