class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        # visited = [[False]*col for _ in range(row)]
        curr = 0
        test =  []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    test.append([i, j])
                    # visited[i][j] = True
                else:
                    matrix[i][j] = row+col
        curr = 1
        x = [1, 0, -1, 0]
        y = [0, 1, 0, -1]
        while test:
            i ,j = test.pop(0)
            for k in range(4):
                nx = i + x[k]
                ny = j + y[k]
                if  nx<row and ny<col and nx>=0 and ny>=0 :
                    if  matrix[nx][ny] > matrix[i][j] + 1:
                        matrix[nx][ny] = matrix[i][j] + 1
                        # visited[nx][ny] == True
                        test.append([nx, ny])
        return matrix
            


