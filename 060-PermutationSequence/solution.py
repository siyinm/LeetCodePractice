class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fac = [1,1,2,2*3,2*3*4,2*3*4*5,2*3*4*5*6,2*3*4*5*6*7,2*3*4*5*6*7*8,2*3*4*5*6*7*8*9]
        avail = [i for i in range(1, n+1)]
        ans = []
        k-=1
        for i in range (n-1, -1, -1):
            d = k//fac[i]  #选的第几位
            k = k % fac[i]
            x = avail[d]
            avail.remove(x)
            ans.append(str(x))
            
        return "".join(ans)
            
