class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def calchilds(perfix: int, k: int) -> int:
            curr = perfix
            nex = curr + 1
            count = 0
            while curr <= k:
                count += min(k+1, nex) - curr
                curr *= 10
                nex *= 10
            return count
        p = 1
        perfix = 1
        while (p < k):
            cnt = calchilds(perfix, n)
            if (cnt + p > k):
                perfix *= 10
                p += 1
            else:
                p = p + cnt
                perfix += 1
                
        return perfix

