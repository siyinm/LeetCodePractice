The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

### Solution:

对每一位数字定位

比如第一位f，是第f组(n-1)!的全排列，可以整除求出是第几组。

设置可用数组1-9构成

每次循环

- k取余数
- 再可用数组中删去上一轮确定的数字，注意整除得到的答案是第几个数字，不是数字本身

tips: 直接用回溯会超时