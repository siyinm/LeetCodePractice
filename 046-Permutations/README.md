## Permuatitons

Given a collection of distinct integers, return all possible permutations.

```{python}
Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

### Solution

[回溯算法详解：](https://leetcode-cn.com/problems/permutations/solution/hui-su-suan-fa-xiang-jie-by-labuladong-2/)

解决一个回溯问题，实际上就是一个决策树的遍历过程。你只需要思考 3 个问题：

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
其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」，

![image](http://github.com/siyinm/LeetCodePractice/raw/master/046-Permutations/pic046.jpeg)

我的做法是第i项数字可以插入在已经放置好的前i-1项中的任意i个位置。

所以对应的选择是插空位置，不需要剪枝

官方使用交换，没这个好理解