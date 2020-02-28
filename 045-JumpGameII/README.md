Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

### Solution

使用最少的步数到达最后一个位置，则第i步位置为第 i−1步前的点中所能达到的最远位置。

#### 贪心算法
定义步数step=0step=0，能达到的最远位置max_bound=0，和上一步到达的边界end=0
遍历数组，遍历范围[0,n-1)：
所能达到的最远位置max\_bound=max(max\_bound,nums[i]+i)，表示上一最远位置和当前索引ii和索引ii上的步数之和中的较大者。
如果索引ii到达了上一步的边界end，则：
更新边界end，令end等于新的最远边界max\_bound，即end=max_bound 令步数step加一
返回step
**注意！**数组遍历范围为[0,n-1)，因为当i= 0时，step已经加一,所以若最后一个元素也遍历的话，当end恰好为n-1，步数会多1。

时间复杂度：$O\left(n\right)$
空间复杂度：$O(1)$

