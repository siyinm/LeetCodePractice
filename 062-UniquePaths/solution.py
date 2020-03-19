class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def fac(i:int) -> int:
            ans = 1
            for i in range(1, i+1, 1):
                ans *= i
            return ans
        u = 1
        res = 1
        for i in range (m, m+n-1,1):
            u *= i
        return  int(u/fac(n-1))


