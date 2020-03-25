On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.

 

Example 1:

```
Input: [[2]]
Output: 10
```


Example 2:

```
Input: [[1,2],[3,4]]
Output: 34
```


Example 3:

```
Input: [[1,0],[0,2]]
Output: 16
```


Example 4:

```
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
```


Example 5:

```
Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46

```

### Solution

写成matrix，类似一个地形平面图，每个位置数字表示高度

先求所有表面积，再减去重合部分 vertically and horizontally