The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

![pic051](http://github.com/siyinm/LeetCodePractice/raw/master/pics/pic051.png)

### Solution

依旧回溯法

1、路径：也就是已经做出的选择。

2、选择列表：也就是你当前可以做的选择。

3、结束条件：也就是到达决策树底层，无法再做选择的条件。

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

### Reference

https://leetcode-cn.com/problems/n-queens/solution/hui-su-suan-fa-xiang-jie-by-labuladong/

