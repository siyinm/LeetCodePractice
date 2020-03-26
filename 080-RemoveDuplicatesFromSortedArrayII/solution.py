class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if not nums: return 0
        # curr = nums[0]
        # count = 0
        # i = 0
        # while i < len(nums): 
        #     if curr == nums[i]:
        #         count += 1
        #         if count > 2:
        #             nums.remove(curr)
        #             count -= 1
        #             i-=1
        #     else:
        #         curr = nums[i]
        #         count = 1
        #     i+=1
        # return len(nums)

        i = 0 
        for n in nums:
            if i < 2 or n != nums[i-2]:
                nums[i] = n
                i += 1
        return i 
