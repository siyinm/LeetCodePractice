Given an unsorted integer array, find the smallest missing positive integer.
duplicated number allowed.

### Solution
规定时间复杂度O(n)=n and 常数空间

发现和数组长度有关，不可能是大于数组长度的数字。

hash map的思想，但是用替换的方法实现，在一个数组中完成映射，以正负表示是否有映射存在

方法：

第一遍，把所有负数换成INT_MAX。

第二遍，将出现的数的绝对值对应的位置的数置为负数。（小于size且为正数）

第三遍，不是负数就输出位置。