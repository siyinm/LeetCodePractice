class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        avg = sum(A)/3
        if avg-int(avg)!= 0 :return False
        if len(A) < 3 :
            return False
        snow = 0
        count = 0
        for i in A:
            snow += i
            if snow == avg:
                count +=1
                snow = 0
        return count >=3


