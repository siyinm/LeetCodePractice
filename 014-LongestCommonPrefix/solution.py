class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        rev=''
        for i in range(len(strs[0])):
            temp=strs[0]
            temp=temp[i]
            for s in strs:
                if len(s)<=i: 
                    return rev
                if s[i]!=temp:
                    return rev
            rev+=temp
        return rev

class Solution2:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        res = s[0]
        i = 1
        while i < len(s):
            while s[i].find(res) != 0:
                res = res[0:len(res)-1]
            i += 1
        return res


