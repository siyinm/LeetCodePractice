class Solution:
    def isMatch(self, s:str, p:str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >=2 and p[1]=="*":
            return (self.isMatch(s, p[2:]) or 
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatch_dp(self, text:str, pattern:str) -> bool:
        memo = dict()
        def dp(i, j):
            if (i,j) in memo:
                return memo[(i, j)]
            if j==len(pattern):
                return i==len(text)
            first_match = i < len(text) and text[i] in {pattern[j], '.'}
            if j<=len(p)-2 and pattern[i+1]=='*':
                ans = dp(i, j+2) or 
                    first_match and dp(i+1, j)
            else:
                ans = first_match and dp(i+1, j+1)
            memo[(i,j)] = ans
            return ans
        return dp(0,0)