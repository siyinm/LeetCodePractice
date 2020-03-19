class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = dict()
        for c in s:
            count[str(c)]=count.get(str(c),0)+1
        m = 0
        s = 0
        odd = 0 
        for k in count:
            v = count.get(k)
            if v%2 == 1:
                odd += 1
                s += v-1
            else:
                s += v
        return s+1 if odd else s
