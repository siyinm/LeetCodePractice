Given an N x N grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.

### Solution

**BFS**

```pseudocode
while queue 不空：
    cur = queue.pop()
    for 节点 in cur的所有相邻节点：
        if 该节点有效且未访问过：
            queue.push(该节点)
```



```pseudocode
level = 0
while queue 不空：
    size = queue.size()
    while (size --) {
        cur = queue.pop()
        for 节点 in cur的所有相邻节点：
            if 该节点有效且未被访问过：
                queue.push(该节点)
    }
    level ++;

作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible/solution/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-sh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

有了计算最短路径的层序 BFS 代码框架，写这道题就很简单了。这道题的主要思路是：

- 一开始，我们找出所有陆地格子，将它们放入队列，作为第 0 层的结点。
- 然后进行 BFS 遍历，每个结点的相邻结点可能是上、下、左、右四个方向的结点，注意判断结点位于网格边界的特殊情况。
- 当遍历结束时，当前的遍历层数就是海洋格子到陆地格子的最远距离。


