class Solution:
    def lastRemaining(self, n: int, m: int) -> int:       
        i, a = 0, list(range(n))
        while len(a)>1:
            i = (i+m-1)%len(a)
            a.pop(i)
        return a[0]


