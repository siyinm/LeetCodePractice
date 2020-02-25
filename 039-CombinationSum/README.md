Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

### Solution

回溯算法应用

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

先排序方便剪枝