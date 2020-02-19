class Solution(object):
    def searchRange(self, nums, target):
        return [self.left_bound(nums,target), self.right_bound(nums,target)]
    def right_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right >= 0 and nums[right] == target: return right # 注意
        else: return -1
    def left_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left <= len(nums)-1 and nums[left] == target: return left  # 注意
        else: return -1
