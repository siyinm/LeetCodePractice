Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
### Soltuion
1. 双指针，一个搜索符合条件的值，一个用来指当前需要覆盖的位置，返回长度所以后面的值不需要考虑删除
2. 删除重复的值
