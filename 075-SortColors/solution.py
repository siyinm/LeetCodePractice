class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        now = 0
        while now <= right:
            if nums[now] == 0:
                nums[left], nums[now] = nums[now], nums[left]
                now += 1
                left += 1
            elif nums[now] == 2:
                nums[right], nums[now] = nums[now], nums[right]
                right -= 1
            elif nums[now] == 1:
                now += 1
            

