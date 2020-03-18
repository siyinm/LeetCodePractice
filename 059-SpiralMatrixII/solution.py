class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for i in range(n)] for j in range(n)]
        c = 1
        j = 0
        while c<=n*n:
            for i in range(j, n-j):
                ans[j][i] = c
                c+=1
            for i in range(j+1, n-j):
                ans[i][n-j-1] = c
                c+=1
            for i in range(n-j-2, j-1, -1):
                ans[n-j-1][i] = c
                c+=1
            for i in range(n-j-2, j, -1):
                ans[i][j] = c
                c+=1
            j += 1
        return ans
