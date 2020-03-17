class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums)
        if l<=1: return True
        maxdis = 0
        for i in range(l):
            if i<= maxdis:
                maxdis = max(maxdis, i+nums[i])
        return maxdis >= l-1

    
