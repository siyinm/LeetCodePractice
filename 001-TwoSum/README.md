## Two sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

### Example

```{cpp}
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```



## Solution

1. 暴力法：**遍历**两遍   

   Time complexity: $ O(n^2) $

   Space complexity: $ O(1) $

2. **Hash table:** 

   key 是num中的值

   value是num的index

   相当于逆转了vector中val和index的对应关系 

   两种使用方法

   Time complexity: $ O(n) $

   Space complexity: $ O(n) $

   - 先初始化hash table，再遍历一次找sum-num[i]，注意排除sum=2num[i]情况

   - 初始化的同时向前寻找sum-num[i]，不需要注意sum=2num[i]

     

     

     
