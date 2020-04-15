Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

### Solution

1. DP
   1. 只看左上和遍历一次，再只看右下
2. BFS
   1. 先遍历一遍找 0 放到栈，多起点b f s（不是0的点用R+C初始化）
   2. while栈为0，该点为四个方向最小值

