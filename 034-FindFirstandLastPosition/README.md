Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

### Solution

分为查找左边界和右边界两个任务来做

注意当nums[mid]==target的时候的执行任务(修改边界)

注意退出循环后，返回前判断是否为-1