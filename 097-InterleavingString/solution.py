class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1+n2 != n3: return False
        dp = [[False]*(n2+1) for _ in range(n1+1)]
        dp[0][0] = True
        for i in range(1, n1+1):
            if s1[:i] == s3[:i]:
                dp[i][0] = True
        for i in range(1, n2+1):
            if s2[:i] == s3[:i]:
                dp[0][i] = True
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if dp[i-1][j]==False and dp[i][j-1]==False:
                    continue
                if dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                    continue
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
        
        return dp[-1][-1]
