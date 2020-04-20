class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        bfs = []
        count = 0
        nrow = len(grid)
        ncol = len(grid[0])
        
        for i in range(nrow):
            for j in range(ncol):
                grid[i][j] = int(grid[i][j])
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] <= 0 :
                    continue
                elif grid[i][j] == 1:
                    count += 1
                    bfs.append((i, j))
                    while bfs:
                        r, c = bfs.pop(0)
                        if r-1 >= 0 and grid[r-1][c] == 1:
                            bfs.append((r-1, c))
                            grid[r-1][c] = -1
                        if c-1 >=0 and grid[r][c-1] == 1:
                            bfs.append((r, c-1))
                            grid[r][c-1] = -1
                        if r+1 < nrow and grid[r+1][c] == 1:
                            bfs.append((r+1, c))
                            grid[r+1][c] = -1
                        if c + 1 < ncol and grid[r][c+1] ==1:
                            bfs.append((r, c+1))
                            grid[r][c+1] = -1    

        return count                      
                            

