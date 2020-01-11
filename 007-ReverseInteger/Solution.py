class Solution1:
    def reverse(self, x: int) -> int:
        ans=int(str(abs(x))[::-1])*(-1 if x<0 else 1)
        return ans if -2**31 <= ans <= 2**31-1 else 0

class Solution2:
    def reverse(self, x: int) -> int:
        y, ans=abs(x), 0
        boundary = (1<<31) -1 if x>0 else 1<<31
        while y!=0:
            ans=ans*10+y%10
            if ans>boundary:
                return 0
            y//=10
        return ans if x>0 else -ans

