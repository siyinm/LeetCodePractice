class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        N = len(s)
        if N > 12:
            return res
        def dfs(dots:int, curr: str, t: str):
            if dots == 0 and t == '':
                res.append(curr[:-1])
                return 
            if len(t) > 0:
                dfs(dots-1, curr+t[0]+'.', t[1:])
            if len(t) > 1 and t[0] != '0':
                dfs(dots-1, curr+t[0:2]+'.', t[2:])
            if len(t) > 2 and t[0] != '0' and int(t[0:3]) < 256:
                dfs(dots-1, curr+t[0:3]+'.', t[3:])
        dfs(4, '', s)

        return res 
        
