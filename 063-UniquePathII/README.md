A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

### Solution

动态规划，在前一题基础上加一点判断条件即可

注意：

- c++过程中会溢出，用long or unit_64t 不要用int
- 第一排第一个也可能是路障