class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        s = 0
        for num in nums:
            s ^= num
        index = 0
        while s & 1 == 0:
            index += 1
            s >>= 1
        r1, r2 = 0, 0
        for num in nums:
            if ( num >> index ) & 1 == 0:
                r1 ^= num
            else:
                r2 ^= num
        return [r1,r2]
