class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        st = []
        b = [0]*len(s)
        dp = [0]*len(s)
        count=0
        for i, val in enumerate(s):
            if val == '(':
                st.append(i)
            elif st:
                b[st.pop()], b[i] = 1,1
        sum = 0
        for i in range(len(s)):
            if b[i]:
                sum+=1
            else:
                sum = 0
            if i>0:
                dp[i] = max(dp[i-1], sum)        
        return dp[len(s)-1]

               
