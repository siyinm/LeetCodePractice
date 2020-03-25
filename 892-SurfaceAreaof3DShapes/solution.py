class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)
        cubes = 0
        faces = 0
        for i in range(N):
            for j in range(N):
                cubes += grid[i][j];
                if grid[i][j] > 1:
                    faces += grid[i][j]-1
                if i > 0:
                    faces += min(grid[i-1][j], grid[i][j])
                if j > 0:
                    faces += min(grid[i][j], grid[i][j-1])
        return 6*cubes-2*faces
