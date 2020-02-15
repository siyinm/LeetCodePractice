class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n<2: return
        i = n-1
        while i>0 and nums[i-1]>=nums[i]:
            i -= 1
        if i==0 and nums[i]==max(nums): 
            return nums.reverse()
        else:                               
            j = n-1
            while j>i-1 and nums[j]<=nums[i-1]:
                j -= 1
            temp = nums[i-1]   
            nums[i-1] = nums[j]
            nums[j] = temp
            re = nums[i:]
            re = re[::-1]
            nums[i:] = re
            return nums

    

