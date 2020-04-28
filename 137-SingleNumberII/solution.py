class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            temp = 1 << i
            count = 0
            for num in nums:
                if num & temp != 0:
                    count +=1
            if count % 3 != 0:
                res |= temp;
        return res - 2 ** 32 if res > 2 ** 31 - 1 else res
