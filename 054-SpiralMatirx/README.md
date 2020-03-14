Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

### Solution

遍历

- 用一个数组```seen```来充当hash map 记录当前点是否被遍历，避免了边界的判断问题
- 用方向矩阵来表示方向，change direction = change index