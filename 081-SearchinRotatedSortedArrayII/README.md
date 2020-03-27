Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

```
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
```


Example 2:

```
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
```


Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?

### Solution

3 conditions:

1. `nums[left] ==nums[mid]` : directly `left++` to eliminate one redundant element
2. `nums[left] < nums[mid]`: the left side is sorted, then judge whether `target` is in the range
3. `nums[left] > nums[mid]`: the right side is sorted