class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        if len(nums)<=2:
            return sum(nums)
        ans=nums[0]+nums[1]+nums[len(nums)-1]
        for i in range(0, len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while(left<right):
                s=nums[left]+nums[right]+nums[i]
                if s==target:
                    return target
                elif s>target:
                    right-=1
                else:
                    left+=1
                if abs(s-target)<abs(ans-target):
                    ans=s  
        return ans