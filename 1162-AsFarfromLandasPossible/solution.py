class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = []
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
        if  len(queue) == 0 or len(queue) == N*N:
            return -1
        distance = -1
        dirx = [1,-1, 0, 0]
        diry = [0, 0, 1, -1]
        while len(queue)>0:
            distance += 1
            n = len(queue)
            for _ in range(n):
                x, y = queue.pop(0)
                for i in range(4):
                    a = x + dirx[i]
                    b = y + diry[i]
                    if a<0 or b<0 or a>=N or b>=N or grid[a][b] != 0:
                        continue
                    grid[a][b] = 2
                    queue.append((a, b))
        return distance
