class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        if len(nums)<=2:
            return []
        for i in range(0, len(nums)):
            if nums[i]>0:
                return ans
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while(left<right):
                if nums[left]+nums[right]+nums[i]==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[left]+nums[right]+nums[i]>0:
                    right-=1
                else:
                    left+=1
        return ans