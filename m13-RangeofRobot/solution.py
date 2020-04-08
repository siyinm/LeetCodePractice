class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = [[0]*n for _ in range(m)]
        def dfs(i:int, j:int) -> int:
            if (i < 0 or  i>=m or j<0 or j>=n or (i//10+i%10+j//10+j%10) > k or visited[i][j] ):
                return 0
            visited[i][j] = 1
            return dfs(i+1, j)+dfs(i,j+1)+1
        return dfs(0,0)

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()
        return self.dfs(0,0, m, n,k, visited)   
    def dfs(self,i, j, m ,n,k,visited) -> int:
        if (i < 0 or  i>=m or j<0 or j>=n or (i//10+i%10+j//10+j%10) > k or (i, j) in visited ):     
            return 0
        visited.add((i,j))    
        return 1+self.dfs(i+1, j,m,n,k,visited)+self.dfs(i,j+1,m,n,k,visited)
