Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.

## Solution
- 数组A的和如果不能被3整除直接返回false
- 遍历数组累加，每累加到目标值count加1，表示又找到1段
- 最后判断是否找到了3段（注意如果目标值是0的话可以大于3段）
