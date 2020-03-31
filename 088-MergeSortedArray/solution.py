class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f = m-1
        s = n-1 
        curr = len(nums1)-1
        while f>=0 and s>=0 and curr>=0:
            if nums1[f]>nums2[s]:
                nums1[curr] = nums1[f]
                f -= 1
            else: 
                nums1[curr] = nums2[s]
                s -= 1
            curr -= 1
        while s>=0:
            nums1[curr] = nums2[s]
            s-=1 
            curr -=1
        
