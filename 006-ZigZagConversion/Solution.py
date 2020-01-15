class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)<=numRows or numRows==1:
            return s
        res = ["" for _ in range(numRows) ]
        flag=1
        curr=0
        instring=1
        for c in s:
            res[curr]+=c
            curr+=flag
            if (instring)%(numRows-1)==0:
                flag*=-1
            instring+=1
        return ''.join(res)